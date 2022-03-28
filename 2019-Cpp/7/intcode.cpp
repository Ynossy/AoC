#include <iostream>
#include <vector>

class IntCode
{
public:
    /**
     * @brief Construct a new Int Code object
     *
     * @param code_array vector containing the initial state
     * @param input_array all inputs, given sequentially
     * @param input_array_len amount of inputs given
     */
    IntCode(std::vector<int> code_array, int *input_array, int input_array_len)
        : code_array(code_array), input_array(input_array), input_array_len(input_array_len)
    {
        i_idx = 0;
    }
    int run();

private:
    std::vector<int> code_array;
    int *input_array;
    int input_array_len;
    int i_idx;
    /**
     * @brief parse integer ABCDE into [DE, C, B, A]
     */
    void parse_inst(int instr, int op_array[])
    {
        op_array[0] = instr % 100;
        op_array[1] = instr / 100 % 10;
        op_array[2] = instr / 1000 % 10;
        op_array[3] = instr / 10000 % 10;
    }
};

int IntCode::run()
{
    int idx = 0;
    int op_array[4];
    parse_inst(code_array[idx++], op_array);

    while (op_array[0] != 99)
    {
        if (op_array[0] == 1)
        {
            // Add
            int op1 = op_array[1] ? code_array[idx++] : code_array[code_array[idx++]];
            int op2 = op_array[2] ? code_array[idx++] : code_array[code_array[idx++]];
            int out = code_array[idx++];
            code_array[out] = op1 + op2;
        }
        else if (op_array[0] == 2)
        {
            // Mult
            int op1 = op_array[1] ? code_array[idx++] : code_array[code_array[idx++]];
            int op2 = op_array[2] ? code_array[idx++] : code_array[code_array[idx++]];
            int out = code_array[idx++];
            code_array[out] = op1 * op2;
        }
        else if (op_array[0] == 3)
        {
            // Input
            // std::cout << "Input Number: (1 for part I, 5 for part II) \n";
            // int manual_input;
            // std::cin >> manual_input;
            int out = code_array[idx++];
            if (i_idx < input_array_len)
            {
                // std::cout << "Input: " << input_array[i_idx] << "\n";
                code_array[out] = input_array[i_idx++];
            }
            else
            {
                std::cerr << "Run out of input values\n";
                return -1;
            }
        }
        else if (op_array[0] == 4)
        {
            // Output
            int out = op_array[1] ? code_array[idx++] : code_array[code_array[idx++]];
            std::cout << "Instruction Output: " << out << "\n";
            return out;
        }
        else if (op_array[0] == 5)
        {
            // Jump if true
            int op1 = op_array[1] ? code_array[idx++] : code_array[code_array[idx++]];
            int op2 = op_array[2] ? code_array[idx++] : code_array[code_array[idx++]];
            idx = op1 ? op2 : idx;
        }
        else if (op_array[0] == 6)
        {
            // Jump if false
            int op1 = op_array[1] ? code_array[idx++] : code_array[code_array[idx++]];
            int op2 = op_array[2] ? code_array[idx++] : code_array[code_array[idx++]];
            idx = op1 ? idx : op2;
        }
        else if (op_array[0] == 7)
        {
            // less than
            int op1 = op_array[1] ? code_array[idx++] : code_array[code_array[idx++]];
            int op2 = op_array[2] ? code_array[idx++] : code_array[code_array[idx++]];
            int out = code_array[idx++];
            code_array[out] = op1 < op2;
        }
        else if (op_array[0] == 8)
        {
            // equal
            int op1 = op_array[1] ? code_array[idx++] : code_array[code_array[idx++]];
            int op2 = op_array[2] ? code_array[idx++] : code_array[code_array[idx++]];
            int out = code_array[idx++];
            code_array[out] = op1 == op2;
        }
        else
        {
            std::cerr << "Invalid Instruction: " << op_array[0] << "\n";
        }
        parse_inst(code_array[idx++], op_array);
    }
    std::cout << "Incode ran without Output!\n";
    return 0;
}