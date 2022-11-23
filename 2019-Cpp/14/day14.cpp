#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>

typedef struct Ingredient
{
    int amount;
    std::string name;
} Ingredient;

typedef struct Reaction
{
    int64_t stock = 0;
    Ingredient result;
    std::vector<Ingredient> ingredients;
} Reaction;

int64_t produce(std::unordered_map<std::string, Reaction> &reaction_list, const std::string &name, int64_t n)
{
    int64_t count = 0;

    auto &reaction = reaction_list[name];

    for (auto &i : reaction.ingredients)
    {
        if (i.name.compare("ORE") == 0)
        {
            count += i.amount * n;
            continue;
        }
        while (reaction_list[i.name].stock < i.amount * n)
        {
            int64_t missing = fmax((i.amount * n - reaction_list[i.name].stock) / reaction_list[i.name].result.amount, 1);
            count += produce(reaction_list, i.name, missing);
        }
        reaction_list[i.name].stock -= i.amount * n;
    }
    reaction_list[name].stock += reaction.result.amount * n;

    return count;
}

int64_t part1(std::unordered_map<std::string, Reaction> reaction_list)
{
    // Result 337862
    int64_t ores = produce(reaction_list, "FUEL", 1);
    std::cout << "Ores needed: " << ores << "\n";
    return ores;
}

void part2(std::unordered_map<std::string, Reaction> reaction_list, int64_t p1)
{
    /** binary search, since its SUPER inefficient to call produce() for a single fuel mutiple times
     *  3687785 too low
     *  3687786 right
     */

    int64_t goal = 1000000000000;
    int64_t l = goal/p1;
    int64_t r = l*100;
    for (int i = 0; i < 200; i++)
    {
        std::unordered_map<std::string, Reaction> copy_l = reaction_list;
        int64_t mid = produce(copy_l, "FUEL", (l + r) / 2);
        std::cout << (l + r) / 2 << " " << mid << "\n";

        if (mid > goal)
        {
            r = (l + r) / 2;
        }
        else if (mid < goal)
        {
            l = (l + r) / 2;
        }

        if (r - l <= 1)
            break;
        // std::cout << l << " " << r << "\n";
    }
    while (true)
    {
        std::unordered_map<std::string, Reaction> copy = reaction_list;
        int64_t mid = produce(copy, "FUEL", r--);
        // std::cout << mid << "\n";
        if (mid < goal)
            break;
    }

    // why +1?
    std::cout << "Produced Amount of Fuel: " << r+1 << "\n";
}

int main()
{
    std::ifstream inputFile("../../14/input.txt");
    // std::ifstream inputFile("../../14/example.txt");

    // input container
    std::unordered_map<std::string, Reaction> reaction_list;

    // ----------------------------------------------
    // Parse input to vector
    std::string line;
    while (std::getline(inputFile, line))
    {
        std::stringstream ss(line);
        std::string ing;

        Reaction reaction;

        while (std::getline(ss, ing, ','))
        {
            // std::cout << ing << "|\n";
            std::stringstream ss2(ing);
            Ingredient ingredient;
            ss2 >> ingredient.amount;
            ss2 >> ingredient.name;
            reaction.ingredients.push_back(ingredient);

            // std::cout << ingredient.amount << "|" << ingredient.name << "|\n";
            // std::cout << "Peek:" << ss2.peek() << "|\n";
            if (ss2.peek() == ' ')
            {
                ss2.ignore(3);
                Ingredient result;
                ss2 >> result.amount;
                ss2 >> result.name;
                reaction.result = result;
                // std::cout << "Results in:" << result.amount << "|" << result.name << "|\n";
            }
        }
        reaction_list.emplace(reaction.result.name, reaction);
    }
    inputFile.close();

    int64_t p1 = part1(reaction_list);
    part2(reaction_list, p1);

    return 0;
}