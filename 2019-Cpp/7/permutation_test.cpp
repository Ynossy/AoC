#include <algorithm>
#include <vector>
#include <iostream>

int main()
{

    std::vector<int> numbers = {0, 1, 2, 3};
    while (std::next_permutation(numbers.begin(), numbers.end()))
    {
        for (int i : numbers)
        {
            std::cout << i << " ";
        }
        std::cout << "\n";
    }
    return 0;
}