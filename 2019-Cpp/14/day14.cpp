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
    Ingredient result;
    std::vector<Ingredient> ingredients;
} Reaction;

/**
 * TODO: Need to keep track of overproduced ores
 */
double get_ore_count(const std::unordered_map<std::string, Reaction> &reaction_list, const std::string &name)
{
    if(name.compare("ORE") == 0){
        return 1;
    }
    double count = 0;
    if (auto search = reaction_list.find(name); search != reaction_list.end())
    {
        auto reaction = search->second;
        for (auto i : reaction.ingredients)
        {
            count += i.amount * get_ore_count(reaction_list, i.name) / static_cast<double>(reaction.result.amount);
        }
    }
    else
    {
        std::cerr << "Element not found: " << name << "\n";
    }

    return count;
}

void part1(std::unordered_map<std::string, Reaction> &reaction_list)
{
    int ores = get_ore_count(reaction_list, "FUEL");
    std::cout << "Ores needed: " << ores << "\n";
}

int main()
{
    // std::ifstream inputFile("../14/input.txt");
    std::ifstream inputFile("../14/example_small.txt");

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

    return 0;
}