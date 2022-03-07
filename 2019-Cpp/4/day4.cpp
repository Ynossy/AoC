#include <iostream>

#define range_L 245318
#define range_H 765747

int part1()
{
    int digits[6] = {0, 0, 0, 0, 0, 0};

    int counter = 0;
    for (int i = range_L; i <= range_H; i++)
    {
        int n = i;
        int div = 100000;
        for (int d = 5; d >= 0; d--)
        {
            digits[d] = n / div;
            n -= digits[d] * div;
            div /= 10;
        }
        bool not_dec = true;
        bool same_dig = false;
        for (int d = 5; d > 0; d--)
        {
            if (digits[d] > digits[d - 1])
            {
                not_dec = false;
            }
            if (digits[d] == digits[d - 1])
            {
                same_dig = true;
            }
        }
        if (not_dec && same_dig)
        {
            counter++;
        }
    }
    return counter;
}

int part2()
{
    int digits[6] = {0, 0, 0, 0, 0, 0};

    int counter = 0;
    for (int i = range_L; i <= range_H; i++)
    {
        int n = i;
        int div = 100000;
        for (int d = 5; d >= 0; d--)
        {
            digits[d] = n / div;
            n -= digits[d] * div;
            div /= 10;
        }
        bool not_dec = true;
        bool same_dig = false;
        int dig_c[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        for (int d = 5; d > 0; d--)
        {
            if (digits[d] > digits[d - 1])
            {
                not_dec = false;
            }
            if (digits[d] == digits[d - 1])
            {
                dig_c[digits[d]] += 1;
            }
        }
        for (int i : dig_c)
        {
            if (i == 1)
                same_dig = true;
        }
        if (not_dec && same_dig)
        {
            counter++;
        }
    }
    return counter;
}

int main()
{

    int c1 = part1();
    int c2 = part2();
    std::cout << "Matching Numbers Part1: " << c1 << "\n";
    std::cout << "Matching Numbers Part2: " << c2;
    return 0;
}