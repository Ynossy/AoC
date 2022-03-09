#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

/**
 * @brief parse integer ABCDE into [DE, C, B, A]
 *
 */
void parse_inst(int instr, int op_array[])
{
    op_array[0] = instr % 100;
    op_array[1] = instr / 100 % 10;
    op_array[2] = instr / 1000 % 10;
    op_array[3] = instr / 10000 % 10;
}

int main()
{
    std::ifstream inputFile("../5/input.txt");

    // input container
    std::vector<int> input;

    std::string line;
    std::getline(inputFile, line);

    std::stringstream ss(line);
    int val;
    while (ss >> val)
    {
        input.push_back(val);
        if (ss.peek() == ',')
            ss.ignore();
    }
    inputFile.close();

    // Part 1
    int idx = 0;
    int op_array[4];
    parse_inst(input[idx++], op_array);

    while (op_array[0] != 99)
    {
        if (op_array[0] == 1)
        {
            // Add
            int op1 = op_array[1] ? input[idx++] : input[input[idx++]];
            int op2 = op_array[2] ? input[idx++] : input[input[idx++]];
            int out = input[idx++];
            input[out] = op1 + op2;
        }
        else if (op_array[0] == 2)
        {
            // Mult
            int op1 = op_array[1] ? input[idx++] : input[input[idx++]];
            int op2 = op_array[2] ? input[idx++] : input[input[idx++]];
            int out = input[idx++];
            input[out] = op1 * op2;
        }
        else if (op_array[0] == 3)
        {
            // Input
            std::cout << "Input Number: ";
            int manual_input;
            std::cin >> manual_input;
            int out = input[idx++];
            input[out] = manual_input;
        }
        else if (op_array[0] == 4)
        {
            // Output
            int out = op_array[1] ? input[idx++] : input[input[idx++]];
            std::cout << "Instruction Output: " << out << "\n";
        }
        else
        {
            std::cout << "Invalid Instruction: " << op_array[0] << "\n";
        }
        parse_inst(input[idx++], op_array);
    }

    return 0;
}