#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

int main()
{
    std::ifstream inputFile("../2/input.txt");

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
    std::vector<int> input_2 = input;
    int idx = 0;
    int opcode = input[idx++];
    while (opcode != 99)
    {
        int op1 = input[idx++];
        int op2 = input[idx++];
        int out = input[idx++];
        if (opcode == 1)
        {
            input[out] = input[op1] + input[op2];
        }
        else if (opcode == 2)
        {
            input[out] = input[op1] * input[op2];
        }
        else
        {
            std::cout << "Unknown Opcode: " << opcode << "\n";
            break;
        }
        opcode = input[idx++];
    }
    std::cout << "Value at first Index: " << input[0];

    // Part 2
    // split line by commas into vector
    std::vector<std::string> input_strings;
    int start = 0;
    int end = 0;
    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] == ',')
        {
            input_strings.push_back(line.substr(start, i - start));
            start = i + 1;
        }
    }
    input_strings[1] = "noun";
    input_strings[2] = "verb";
    idx = 0;
    opcode = input_2[idx++];
    while (opcode != 99)
    {
        int op1 = input_2[idx++];
        int op2 = input_2[idx++];
        int out = input_2[idx++];
        if (opcode == 1)
        {
            input_2[out] = input_2[op1] + input_2[op2];
            input_strings[out] = "(" + input_strings[op1] + "+" + input_strings[op2] + ")";
        }
        else if (opcode == 2)
        {
            input_2[out] = input_2[op1] * input_2[op2];
            input_strings[out] = input_strings[op1] + "*" + input_strings[op2];
        }
        else
        {
            std::cout << "Unknown Opcode: " << opcode << "\n";
            break;
        }
        opcode = input_2[idx++];
    }
    std::cout << "Full calculation: " << input_strings[0];
    // verb + 360'000*noun + 610'685 = 19'690'720
    // verb + 360'000*noun = 19'080'035
    // verb + 360'000*53 = 19'080'035
    // 35 + 360'000*53 = 19'080'035
    // solution:  5335

    return 0;
}