#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "intcode.h"

void part1(std::vector<long> input)
{
    // 273 Blocks
    IntCode pc(input);
    int instruction[3];
    int blocks = 0;
    while (true)
    {
        for (int i = 0; i < 3; i++)
        {
            instruction[i] = pc.run();
        }
        if(instruction[2] == 2)
            blocks++;
        if (instruction[0] == -99)
            break;
    }
    std::cout << "Blocks: " << blocks << "\n";
}

void part2(std::vector<long> input)
{
}

int main()
{
    std::ifstream inputFile("../13/input.txt");

    // input container
    std::vector<long> input;

    // ----------------------------------------------
    // Parse input to vector
    std::string line;
    std::getline(inputFile, line);
    std::stringstream ss(line);
    long val;
    while (ss >> val)
    {
        input.push_back(val);
        if (ss.peek() == ',')
            ss.ignore();
    }
    inputFile.close();

    part1(input);
    part2(input);
    return 0;
}