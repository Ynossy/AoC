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

void run(std::vector<long> &input, std::unordered_map<Point, long, Point::HashFunction> &map, long start_color){
    IntCode pc(input);
    pc.push_input(start_color);
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

void part1(std::vector<long> input)
{
    // 8548 too high
    // 2428 correct
    std::unordered_map<Point, long, Point::HashFunction> map;
    run(input, map, 0);
}

void part2(std::vector<long> input)
{
    // RJLFBUCU
    // .###....##.#....####.###..#..#..##..#..#...
    // .#..#....#.#....#....#..#.#..#.#..#.#..#...
    // .#..#....#.#....###..###..#..#.#....#..#...
    // .###.....#.#....#....#..#.#..#.#....#..#...
    // .#.#..#..#.#....#....#..#.#..#.#..#.#..#...
    // .#..#..##..####.#....###...##...##...##....
    std::unordered_map<Point, long, Point::HashFunction> map;
    run(input, map, 1);
    int max_x = INT16_MIN;
    int min_x = INT16_MAX;
    int max_y = INT16_MIN;
    int min_y = INT16_MAX;

    for(auto p: map){
        max_x = p.first.x > max_x ? p.first.x : max_x;
        min_x = p.first.x < min_x ? p.first.x : min_x;
        max_y = p.first.y > max_y ? p.first.y : max_y;
        min_y = p.first.y < min_y ? p.first.y : min_y;
    }
    std::cout << max_x << " " << min_x << " " << max_y << " " << min_y << "\n";
    int size_x = 1+max_x-min_x;
    int size_y = 1+max_y-min_y;
    std::vector<std::vector<long>> drawing(size_y, std::vector<long>(size_x));
    for(auto p: map){
        int x = p.first.x;
        int y = p.first.y;
        drawing.at(y-min_y).at(x-min_x) = p.second;
    }

    for(int i=size_y-1; i>=0; i--){
        for(auto j:drawing.at(i)){
            std::cout << (j ? '#' : '.');
        }
        std::cout << "\n";
    }


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
    part2(input);
    return 0;
}