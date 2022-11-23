#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <math.h>

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
    // std::cout << "1";
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
            int64_t missing = fmax((i.amount * n -reaction_list[i.name].stock) / reaction_list[i.name].result.amount, 1);
            count += produce(reaction_list, i.name, missing);
        }
        reaction_list[i.name].stock -= i.amount * n;
    }
    reaction_list[name].stock += reaction.result.amount * n;

    return count;
}

void part1(std::unordered_map<std::string, Reaction> reaction_list)
{
    // Result 337862
    int64_t ores = produce(reaction_list, "FUEL", 1);
    std::cout << "Ores needed: " << ores << "\n";
}

void part2(std::unordered_map<std::string, Reaction> reaction_list)
{

    std::unordered_map<std::string, Reaction> copy = reaction_list;
    
    // std::cout << INT_MAX << "\n";
    std::cout << produce(copy, "FUEL", 10000000000) << "\n";
    

    // // takes forever
    // int64_t ores = 1000000000000;
    // int fuel = 0;
    // while (ores > 0)
    // {
    //     ores -= produce(reaction_list, "FUEL", 1);
    //     fuel++;
    //     if (fuel % 1000 == 0)
    //         std::cout << ores << "\n";
    // }
    // fuel -= 1;

    // std::cout << "Produced Amount of Fuel: " << fuel << "\n";
}

int main()
{
    std::ifstream inputFile("../14/input.txt");
    // std::ifstream inputFile("../14/example.txt");

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

    part1(reaction_list);
    part2(reaction_list);

    return 0;
}