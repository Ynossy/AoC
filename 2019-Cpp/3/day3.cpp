#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <set>

void getCommands(std::vector<std::tuple<char, int>> *commands, std::string input)
{
    int start = 0;
    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] == ',')
        {
            char instr = input[start];
            int num = std::stoi(input.substr(start + 1, i - start));
            commands->push_back(std::make_tuple(instr, num));
            start = i + 1;
        }
    }
}

int main()
{
    std::ifstream inputFile("../3/input.txt");

    // input container
    std::vector<std::tuple<char, int>> commands1;
    std::vector<std::tuple<char, int>> commands2;

    std::string line1;
    std::string line2;

    std::getline(inputFile, line1);
    std::getline(inputFile, line2);

    // parse input into <direction, distance> pairs
    getCommands(&commands1, line1);
    getCommands(&commands2, line2);

    // walk over all positions and insert in set, save collisions
    std::set<std::tuple<int, int>> map;
    for (std::tuple<char, int> cmd : commands1)
    {
        int dir[2] = {0, 0};
        switch (std::get<0>(cmd))
        {
        case 'R':
            dir[0] = 1;
            break;
        case 'L':
            dir[0] = -1;
            break;
        case 'U':
            dir[1] = 1;
            break;
        case 'D':
            dir[1] = -1;
            break;
        default:
            std::cout << "Unknown Direction: " << std::get<0>(cmd);
        }
        
        // work in progress
    }

    int start = 0;

    inputFile.close();

    return 0;
}