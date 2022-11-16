#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "intcode.h"
#include <unordered_map>

// https://stackoverflow.com/questions/38554083/how-can-i-use-a-c-unordered-set-for-a-custom-class
struct Point
{
    int x;
    int y;

    Point() {}
    Point(int x, int y)
    {
        this->x = x;
        this->y = y;
    }

    bool operator==(const Point &otherPoint) const
    {
        if (this->x == otherPoint.x && this->y == otherPoint.y)
            return true;
        else
            return false;
    }

    struct HashFunction
    {
        size_t operator()(const Point &point) const
        {
            size_t xHash = std::hash<int>()(point.x);
            size_t yHash = std::hash<int>()(point.y) << 1;
            return xHash ^ yHash;
        }
    };
};

void part1(std::vector<long> input)
{
    // 8548 too high
    // 2428 correct
    std::unordered_map<Point, long, Point::HashFunction> map;

    IntCode pc(input);
    pc.push_input(0);
    int x = 0;
    int y = 0;
    int dir = 0; // 0: UP, 1: RIGHT, 2: DOWN, 3: LEFT
    int dir_x[] = {0, 1, 0, -1};
    int dir_y[] = {1, 0, -1, 0};
    int panel_count = 0;
    while (true)
    {
        long code1 = pc.run();
        long code2 = pc.run();
        // std::cout << code1 << " - " << code2 << "\n";
        if (code1 < 0 || code2 < 0)
        {
            std::cout << "Drawing count: " << panel_count << "\n";
            break;
        }
        bool info = std::get<1>(map.insert_or_assign(Point(x, y), code1));
        if (info)
        {
            panel_count++;
        }
        dir += code2 ? 1 : -1;
        dir = dir % 4;
        if(dir < 0)
            dir+=4;

        x += dir_x[dir];
        y += dir_y[dir];

        auto search = map.find(Point(x, y));
        if (search != map.end())
        {
            pc.push_input(search->second);
        }
        else
        {
            pc.push_input(0);
        }
    }
}

void part2(std::vector<long> input)
{
}

int main()
{
    std::ifstream inputFile("../11/input.txt");

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
    // part2(input);
    return 0;
}