#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <map>
#include <math.h>

void getCommands(std::vector<std::tuple<char, int>> *commands, std::string input)
{
    int start = 0;
    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] == ',' || i == input.length() - 1)
        {
            char instr = input[start];
            int num = std::stoi(input.substr(start + 1, i - start));
            commands->push_back(std::make_tuple(instr, num));
            start = i + 1;
        }
    }
}

void insertLine(std::map<std::tuple<int, int>, int> *map, std::vector<std::tuple<char, int>> *commands)
{
    int pos[2] = {0, 0};
    int delay = 0;
    for (std::tuple<char, int> cmd : *commands)
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
        int dist = std::get<1>(cmd);
        // work in progress
        for (int i = 0; i < dist; i++)
        {
            delay += 1;
            pos[0] += dir[0];
            pos[1] += dir[1];
            auto res = map->emplace(std::make_tuple(pos[0], pos[1]), delay);
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

    inputFile.close();

    // parse input into <direction, distance> pairs
    getCommands(&commands1, line1);
    getCommands(&commands2, line2);

    // walk over all positions and insert in a map each
    std::map<std::tuple<int, int>, int> map1;
    std::map<std::tuple<int, int>, int> map2;
    insertLine(&map1, &commands1);
    insertLine(&map2, &commands2);

    // merge both sets (avoids collisions between the same line)
    int min_hattan = INT_MAX;
    int min_delay = INT_MAX;
    for (auto p : map1)
    {
        auto res = map2.emplace(p);
        if (!res.second)
        {
            auto tuple = *res.first;
            int dist = tuple.second + p.second;
            int d = std::abs(std::get<0>(tuple.first)) + std::abs(std::get<1>(tuple.first));
            if (d < min_hattan)
            {
                min_hattan = d;
                // std::cout << d << "\n";
            }
            if (dist < min_delay)
            {
                min_delay = dist;
            }
        }
    }
    std::cout << "Smallest Distance: " << min_hattan;
    std::cout << ", Smallest delay: " << min_delay;

    return 0;
}