#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "intcode.cpp"

int run_amplifiers(std::vector<int> &input, int phase_settings[]){
    int amp_out = 0;
    for (int i = 0; i < 5; i++)
    {
        int in_a[] = {phase_settings[i], amp_out};//{amp_out, phase_settings[i]};
        IntCode Amp = IntCode(input, in_a, 2);
        amp_out = Amp.run();
    }
    std::cout << "Amplifier Output: " << amp_out << "\n";
    return amp_out;
}
int main()
{
    // std::ifstream inputFile("../7/input.txt");
    std::ifstream inputFile("../7/example.txt");

    // input container
    std::vector<int> input;

    // ----------------------------------------------
    // Parse input to vector
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

    int phase_settings[] = {1,0,4,3,2};
    int amp_out = run_amplifiers(input, phase_settings);

    return 0;
}