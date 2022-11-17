#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <chrono>
#include <thread>

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
        if (instruction[2] == 2)
            blocks++;
        if (instruction[0] == -99)
            break;
    }
    std::cout << "Blocks: " << blocks << "\n";
}

void print_screen(std::vector<std::vector<int>> screen, int score)
{
    std::string s = "";
    for (auto l : screen)
    {
        for (int px : l)
        {
            switch (px)
            {
            case 0:
                s += " ";
                break;
            case 1:
                s += "|";
                break;
            case 2:
                s += "#";
                break;
            case 3:
                s += "_";
                break;
            case 4:
                s += "O";
                break;
            }
            s += " ";
        }
        s += "\n";
    }
    s += "------";
    s += std::to_string(score);
    s += "------\n\n\n\n\n\n\n\n\n";

    std::cout << std::flush;
    std::cout << s;
}

void part2(std::vector<long> input)
{
    input[0] = 2;
    IntCode pc(input);
    int instruction[3];

    int score = 0;
    bool start = false;

    std::vector<std::vector<int>> screen(24, std::vector<int>(42));
    while (true)
    {
        for (int i = 0; i < 3; i++)
        {
            instruction[i] = pc.run();
        }
        if (instruction[0] == -99)
            break;
        if (instruction[0] == -1)
        {
            score = instruction[2];
        }
        else
        {
            if (instruction[1] == 23 && instruction[0] == 41)
            {
                start = true;
            }
            screen.at(instruction[1]).at(instruction[0]) = instruction[2];
        }
        if (start)
        {
            print_screen(screen, score);
            std::this_thread::sleep_for(std::chrono::milliseconds(500));
        }
    }
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