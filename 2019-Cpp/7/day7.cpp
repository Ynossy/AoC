#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "intcode.cpp"

int run_amplifiers(std::vector<int> &input, std::vector<int> &phase_settings)
{
    int amp_out = 0;
    for (int i = 0; i < 5; i++)
    {
        int in_a[] = {phase_settings[i], amp_out}; //{amp_out, phase_settings[i]};
        IntCode Amp = IntCode(input, in_a, 2);
        amp_out = Amp.run();
    }
    // std::cout << "Amplifier Output: " << amp_out << "\n";
    return amp_out;
}

void part1(std::vector<int> &input){
    std::vector<int> phase_settings; // = {1, 0, 4, 3, 2};
    int max = 0;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (j == i)
                continue;
            for (int k = 0; k < 5; k++)
            {
                if (k == i || k == j)
                    continue;
                for (int l = 0; l < 5; l++)
                {
                    if (l == i || l == j || l == k)
                        continue;
                    for (int m = 0; m < 5; m++)
                    {
                        if (m == i || m == j || m == k || m == l)
                            continue;
                        phase_settings = {i, j, k, l, m};

                        // std::cout << i << " " << j << " " << k << " " << l << " " << m << "\n";
                        int amp_out = run_amplifiers(input, phase_settings);
                        if (amp_out > max)
                        {
                            max = amp_out;
                        }
                    }
                }
            }
        }
    }
    // 977932 too high
    // 212460 Right
    std::cout << "Max Output: " << max;
}

part2(std::vector<int> &input){

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