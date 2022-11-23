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
    int stock = 0;
    Ingredient result;
    std::vector<Ingredient> ingredients;
} Reaction;

/**
 * TODO: Need to keep track of overproduced ores
 */

int get_stock(std::unordered_map<std::string, Reaction> &reaction_list, const std::string &name)
{
    if (auto search = reaction_list.find(name); search != reaction_list.end())
    {
        auto reaction = search->second;
        return reaction.stock;
    }
    std::cerr << "Element not found: " << name << "\n";
    return 0;
}

void pop_stock(std::unordered_map<std::string, Reaction> &reaction_list, const std::string &name, int amount)
{
    if (auto search = reaction_list.find(name); search != reaction_list.end())
        search->second.stock -= amount;
    else
        std::cerr << "Element not found: " << name << "\n";
}

void add_stock(std::unordered_map<std::string, Reaction> &reaction_list, const std::string &name, int amount)
{
    if (auto search = reaction_list.find(name); search != reaction_list.end())
        search->second.stock += amount;
    else
        std::cerr << "Element not found: " << name << "\n";
}

int produce(std::unordered_map<std::string, Reaction> &reaction_list, const std::string &name)
{
    int count = 0;
    if (auto search = reaction_list.find(name); search != reaction_list.end())
    {
        auto reaction = search->second;
        for (auto i : reaction.ingredients)
        {
            if (i.name.compare("ORE") == 0)
            {
                count += i.amount;
                continue;
            }
            while (get_stock(reaction_list, i.name) < i.amount)
            {
                count += produce(reaction_list, i.name);
            }
            pop_stock(reaction_list, i.name, i.amount);
        }
        add_stock(reaction_list, name, reaction.result.amount);
    }
    else
    {
        std::cerr << "Element not found: " << name << "\n";
    }
    return count;
}

void part1(std::unordered_map<std::string, Reaction> &reaction_list)
{
    // Result 337862
    int ores = produce(reaction_list, "FUEL");
    std::cout << "Ores needed: " << ores << "\n";
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

    return 0;
}