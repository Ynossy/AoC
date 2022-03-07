#include <iostream>
#include <chrono>

#define range_L 245318
#define range_H 765747

/**
 * @brief check conditions for part 1 or 2
 *
 * @param part2 1 for part2 condition, else 0
 * @return int counted numbers
 */
int check_condiitons(int part)
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
            if (part == 2 && i == 1)
                same_dig = true;
            else if (part == 1 && i > 0)
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
    auto t1 =std::chrono::high_resolution_clock::now();
    int c1 = check_condiitons(1);
    int c2 = check_condiitons(2);
    auto t2 =std::chrono::high_resolution_clock::now();
    auto ms_int = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);

    std::cout << "Matching Numbers Part1: " << c1 << "\n";
    std::cout << "Matching Numbers Part2: " << c2 << "\n";

    std::cout << "Runtime: " << ms_int.count() << "ms";
    return 0;
}