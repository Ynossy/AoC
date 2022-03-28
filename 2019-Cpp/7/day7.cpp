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
        int in_a[] = {phase_settings[i], amp_out};
        IntCode Amp = IntCode(input, in_a, 2);
        amp_out = Amp.run();
    }
    // std::cout << "Amplifier Output: " << amp_out << "\n";
    return amp_out;
}

int loop_amplifiers(std::vector<int> &input, std::vector<int> &phase_settings)
{
    int amp_out = 0;
    int amp_E = 0;
    IntCode AmpA = IntCode(input);
    IntCode AmpB = IntCode(input);
    IntCode AmpC = IntCode(input);
    IntCode AmpD = IntCode(input);
    IntCode AmpE = IntCode(input);
    int in_a[] = {phase_settings[0], amp_out};
    AmpA.set_input(in_a, 2);
    amp_out = AmpA.run();
    int in_b[] = {phase_settings[1], amp_out};
    AmpB.set_input(in_b, 2);
    amp_out = AmpB.run();
    int in_c[] = {phase_settings[2], amp_out};
    AmpC.set_input(in_c, 2);
    amp_out = AmpC.run();
    int in_d[] = {phase_settings[3], amp_out};
    AmpD.set_input(in_d, 2);
    amp_out = AmpD.run();
    int in_e[] = {phase_settings[4], amp_out};
    AmpE.set_input(in_e, 2);
    amp_out = AmpE.run();
    for (int i = 0; i < 1000; i++)
    {
        int in_a[] = {amp_out};
        AmpA.set_input(in_a, 1);
        amp_out = AmpA.run();
        int in_b[] = {amp_out};
        AmpB.set_input(in_b, 1);
        amp_out = AmpB.run();
        int in_c[] = {amp_out};
        AmpC.set_input(in_c, 1);
        amp_out = AmpC.run();
        int in_d[] = {amp_out};
        AmpD.set_input(in_d, 1);
        amp_out = AmpD.run();
        int in_e[] = {amp_out};
        AmpE.set_input(in_e, 1);
        amp_out = AmpE.run();

        if (amp_out == -2)
        {
            // std::cout << "Loops: " << i << "\n";
            break;
        }
        amp_E = amp_out;
    }
    return amp_E;
}

int brute_force_phase(int part, std::vector<int> &input)
{
    int offset = (part == 2) ? 5 : 0;
    std::vector<int> phase_settings;
    int max = 0;
    for (int i = offset; i < offset + 5; i++)
    {
        for (int j = offset; j < offset + 5; j++)
        {
            if (j == i)
                continue;
            for (int k = offset; k < offset + 5; k++)
            {
                if (k == i || k == j)
                    continue;
                for (int l = offset; l < offset + 5; l++)
                {
                    if (l == i || l == j || l == k)
                        continue;
                    for (int m = offset; m < offset + 5; m++)
                    {
                        if (m == i || m == j || m == k || m == l)
                            continue;
                        phase_settings = {i, j, k, l, m};
                        int amp_out;
                        if (part == 1)
                        {
                            amp_out = run_amplifiers(input, phase_settings);
                        }
                        else if (part == 2)
                        {
                            amp_out = loop_amplifiers(input, phase_settings);
                        }
                        if (amp_out > max)
                        {
                            max = amp_out;
                        }
                    }
                }
            }
        }
    }
    return max;
}

void part1(std::vector<int> &input)
{
    int max = brute_force_phase(1, input);
    // 977932 too high
    // 212460 Right
    std::cout << "P1 - Max Output: " << max << "\n";
}

void part2(std::vector<int> &input)
{
    int max = brute_force_phase(2, input);
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