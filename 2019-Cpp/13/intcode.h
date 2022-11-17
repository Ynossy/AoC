#include <iostream>
#include <vector>
#include <deque>
class IntCode
{
public:
    /**
     * @brief Construct a new Int Code object
     *
     * @param code_array vector containing the initial state
     */
    IntCode(std::vector<long> code_array)
        : code_array(code_array)
    {
        idx = 0;
        relative_base = 0;
    }
    long run();

    void set_joystick(int pos){
        joystick = pos;
    }

private:
    std::vector<long> code_array;
    std::deque<long> inputs;
    long joystick = 0;
    long idx; // current programm state
    long relative_base; // relative base for mode 2
    /**
     * @brief parse integer ABCDE into [DE, C, B, A]
     */
    void parse_inst(long instr, long op_array[])
    {
        op_array[0] = instr % 100;
        op_array[1] = instr / 100 % 10;
        op_array[2] = instr / 1000 % 10;
        op_array[3] = instr / 10000 % 10;
    }

    /**
     * @brief Get argument in specific mode:
     *  0 - position -- interpret as position
     *  1 - immediate -- interprete as value
     *  2 - relative -- interpret as relative to relative base paramter
     * 
     * @param mode 
     * @return long 
     */
    long get_argument(long mode){
        if(mode == 0){
            long i = code_array[idx++];
            return code_array[i];
        } else if (mode == 1){
            long i = idx++;
            return code_array[i];
        } else if (mode == 2){
            long i = relative_base + code_array[idx++];
            return code_array[i];
        } else {
            std::cout << "Invalid Argument Mode: " << mode ;
            return -1;
        }        
    }

    long write_argument(long mode){
        if(mode == 0){
            return code_array[idx++];
        } else if (mode == 2) {
            return code_array[idx++] + relative_base;
        } else {
            std::cout << "Cannot write in immediate mode" << "\n";
            return -1;
        }
    }

    void write_to_memory(long idx, long value){
        while (code_array.size() < idx+1){
            code_array.push_back(0);
        }
        code_array[idx] = value;
    }
};

long IntCode::run()
{
    long op_array[4];
    parse_inst(code_array[idx++], op_array);
    long output = -1;

    while (op_array[0] != 99)
    {
        if (op_array[0] == 1)
        {
            // Add
            long op1 = get_argument(op_array[1]);
            long op2 = get_argument(op_array[2]);
            long out = write_argument(op_array[3]);
            write_to_memory(out, op1 + op2);
        }
        else if (op_array[0] == 2)
        {
            // Mult
            long op1 = get_argument(op_array[1]);
            long op2 = get_argument(op_array[2]);
            long out = write_argument(op_array[3]);
            write_to_memory(out, op1 * op2);
        }
        else if (op_array[0] == 3)
        {
            // Input
            long out = write_argument(op_array[1]);
            write_to_memory(out, joystick);
            inputs.pop_front();
        }
        else if (op_array[0] == 4)
        {
            // Output
            output = get_argument(op_array[1]);
            // std::cout << "Instruction Output: " << output << "\n";
            return output;
        }
        else if (op_array[0] == 5)
        {
            // Jump if true
            long op1 = get_argument(op_array[1]);
            long op2 = get_argument(op_array[2]);
            idx = op1 ? op2 : idx;
        }
        else if (op_array[0] == 6)
        {
            // Jump if false
            long op1 = get_argument(op_array[1]);
            long op2 = get_argument(op_array[2]);
            idx = op1 ? idx : op2;
        }
        else if (op_array[0] == 7)
        {
            // less than
            long op1 = get_argument(op_array[1]);
            long op2 = get_argument(op_array[2]);
            long out = write_argument(op_array[3]);
            write_to_memory(out, op1 < op2);
        }
        else if (op_array[0] == 8)
        {
            // equal
            long op1 = get_argument(op_array[1]);
            long op2 = get_argument(op_array[2]);
            long out = write_argument(op_array[3]);
            write_to_memory(out, op1 == op2);
        }
        else if (op_array[0] == 9)
        {
            relative_base += get_argument(op_array[1]);
        }
        else
        {
            std::cerr << "Invalid Instruction: " << op_array[0] << "\n";
        }
        parse_inst(code_array[idx++], op_array);
    }
    // std::cout << "Intcode ran without Output!\n";
    return -99;
}