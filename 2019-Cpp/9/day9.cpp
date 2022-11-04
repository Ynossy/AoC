#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "intcode.h"


void part1(std::vector<long> input){
    IntCode pc(input);
    pc.push_input(1); // testmode input
    pc.run();
}

void part2(std::vector<long> input){
    IntCode pc(input);
    pc.push_input(2); // testmode input
    pc.run();
}

int main(){
    std::ifstream inputFile("../9/input.txt");
    // std::ifstream inputFile("../9/example1.txt");

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