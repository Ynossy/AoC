#include <iostream>
#include <chrono>

#define range_L 245318
#define range_H 765747

void count_up(int digits[], int idx)
{
    digits[idx] += 1;
    if (digits[idx] > 9)
    {
        digits[idx] = 0;
        count_up(digits, idx - 1);
    }
}
/**
 * @brief check conditions for part 1 or 2
 *
 * @param part2 1 for part2 condition, else 0
 * @return int counted numbers
 */
int check_condiitons(int part)
{
    int digits[6] = {2, 4, 5, 3, 1, 8};

    int counter = 0;
    for (int i = range_L; i <= range_H; i++)
    {
        count_up(digits, 5);
        bool not_dec = true;
        bool same_dig = false;
        int dig_c[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        for (int d = 0; d < 5; d++)
        {
            if (digits[d] > digits[d + 1])
            {
                not_dec = false;
                break;
            }
            if (digits[d] == digits[d + 1])
            {
                dig_c[digits[d]] += 1;
            }
            if (d == 4)
                for (int i : dig_c)
                {
                    if (part == 2 && i == 1)
                        same_dig = true;
                    else if (part == 1 && i > 0)
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

int main()
{
    auto t1 = std::chrono::high_resolution_clock::now();
    int c1 = check_condiitons(1);
    int c2 = check_condiitons(2);
    auto t2 = std::chrono::high_resolution_clock::now();
    auto ms_int = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1);

    std::cout << "Matching Numbers Part1: " << c1 << "\n";
    std::cout << "Matching Numbers Part2: " << c2 << "\n";

    std::cout << "Runtime: " << ms_int.count() << "us";
    return 0;
}