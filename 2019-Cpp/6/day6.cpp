#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <chrono>

struct Node
{
    std::string parent;
    std::vector<std::string> childs;
};

void populate_map(std::unordered_map<std::string, Node> &nodes)
{
    std::ifstream file("../6/input.txt");
    // To run example change substrings to 1 length and change part 2 from YOU->Y SAN->S
    // std::ifstream file("../6/example.txt");

    std::string line;

    while (std::getline(file, line))
    {
        std::string parent = line.substr(0, 3);
        std::string child = line.substr(4, 3);
        // std::string parent = line.substr(0, 1);
        // std::string child = line.substr(2, 1);

        auto c_node = nodes.find(child);
        if (c_node == nodes.end())
        {
            Node node = {parent, std::vector<std::string>{}};
            nodes.emplace(child, node);
        }
        else if (!c_node->second.parent.compare("0"))
        {
            c_node->second.parent = parent;
        }

        auto p_node = nodes.find(parent);
        if (p_node == nodes.end())
        {
            Node node = {"0", std::vector<std::string>{child}};
            nodes.emplace(parent, node);
        }
        else
        {
            (p_node->second).childs.push_back(child);
        }
    }
}

int get_orbits(std::unordered_map<std::string, Node> &nodes, std::string key)
{
    int orbits = 0;
    auto node = nodes.find(key);
    while ((node->second.parent).compare("0"))
    {
        node = nodes.find(node->second.parent);
        orbits++;
    }
    return orbits;
}

void part1(std::unordered_map<std::string, Node> &nodes)
{
    int p1 = 0;
    for (auto node : nodes)
    {
        p1 += get_orbits(nodes, node.first);
    }
    std::cout << "Orbits Amount: " << p1 << "\n";
}

void part2(std::unordered_map<std::string, Node> &nodes)
{
    // Walk upwards from YOU and save all nodes with distance in map
    std::unordered_map<std::string, int> you_orbits;
    int n = 0;
    auto node = nodes.find("YOU");
    while ((node->second.parent).compare("0"))
    {
        node = nodes.find(node->second.parent);
        you_orbits.emplace(node->first, n++);
    }

    // Walk upwards from SAN until paths cross
    auto san = nodes.find("SAN");
    n = 0;
    while ((san->second.parent).compare("0"))
    {
        san = nodes.find(san->second.parent);

        auto same = you_orbits.find(san->first);
        if (same != you_orbits.end())
        {
            n += same->second;
            break;
        }
        n++;
    }
    std::cout << "Orbital Swaps: " << n << "\n";
}

int main()
{
    auto t1 = std::chrono::high_resolution_clock::now();

    std::unordered_map<std::string, Node> nodes;
    populate_map(nodes);

    // Task 1
    part1(nodes);

    // Part 2
    part2(nodes);

    auto t2 = std::chrono::high_resolution_clock::now();
    auto ms_int = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);
    std::cout << "Runtime: " << ms_int.count() << "ms";
    return 0;
}