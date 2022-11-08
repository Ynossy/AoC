#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>


void part1(std::vector<long> input){

}

void part2(std::vector<long> input){

}

int main(){
    std::ifstream inputFile("../10/input.txt");

    // input container
    std::vector<std::vector<int>> input;

    // ----------------------------------------------
    // Parse input to vector
    std::string line;
    while (std::getline(inputFile, line))
    {
        input.push_back(std::vector<int>());

        for(char c: line){
            input.at(input.size()-1).push_back(c == '#' ? 1 : 0);
        }
    }
    inputFile.close();

    // part1(input);
    // part2(input);
    return 0;
}