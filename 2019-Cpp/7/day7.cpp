#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include "intcode.cpp"

int run_amplifiers(std::vector<int> &input, std::vector<int> &phase_settings)
{
    int amp_out = 0;
    for (int i = 0; i < 5; i++)
    {
        IntCode amp = IntCode(input);
        amp.push_input(phase_settings[i]);
        amp.push_input(amp_out);
        amp_out = amp.run();
    }
    // std::cout << "Amplifier Output: " << amp_out << "\n";
    return amp_out;
}

int loop_amplifiers(std::vector<int> &input, std::vector<int> &phase_settings)
{
    int amp_out = 0;
    int amp_E = 0;
    std::vector<IntCode> amps;
    for (int i = 0; i < 5; i++)
    {
        amps.push_back(IntCode(input));
        amps[i].push_input(phase_settings[i]);
    }
    while(amp_out != -2)
    {
        amp_E = amp_out;
        for (IntCode &amp: amps)
        {
            amp.push_input(amp_out);
            amp_out = amp.run();
        }
    }
    return amp_E;
}

void part1(std::vector<int> &input)
{
    std::vector<int> phase_settings;
    phase_settings = {0, 1, 2, 3, 4};

    int max = 0;
    while (std::next_permutation(phase_settings.begin(), phase_settings.end()))
    {
        int amp_out;
        amp_out = run_amplifiers(input, phase_settings);
        if (amp_out > max)
        {
            max = amp_out;
        }
    }
    // 977932 too high
    // 212460 Right
    std::cout << "P1 - Max Output: " << max << "\n";
}

void part2(std::vector<int> &input)
{
    std::vector<int> phase_settings;
    phase_settings = {5, 6, 7, 8, 9};

    int max = 0;
    while (std::next_permutation(phase_settings.begin(), phase_settings.end()))
    {
        int amp_out;
        amp_out = loop_amplifiers(input, phase_settings);
        if (amp_out > max)
        {
            max = amp_out;
        }
    }
    // 21844737
    std::cout << "P2 - Max Output: " << max;
}

int main()
{
    std::ifstream inputFile("../7/input.txt");
    // std::ifstream inputFile("../7/example.txt");

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

    part1(input);
    part2(input);
    return 0;
}