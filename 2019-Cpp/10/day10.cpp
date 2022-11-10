#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <tuple>
#include <map>
#include <cmath>

typedef struct t_point
{
    int x;
    int y;
} t_point;

/**
 * Greatest common divisor
 */
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int check_direction(std::vector<std::vector<int>> &input, int r, int c, int x, int y)
{
    if (gcd(abs(y), abs(x)) > 1) // skip direction xy
        return 0;

    int i = r + x;
    int j = c + y;
    while (0 <= i && i < input.size() && 0 <= j && j < input.at(0).size())
    {
        if (input.at(i).at(j))
        {
            return 1;
        }
        i += x;
        j += y;
    }
    return 0;
}

int count_asteroids(std::vector<std::vector<int>> &input, int r, int c)
{
    if (!input.at(r).at(c))
        return 0;

    int asteroids = 0;
    for (int i = 0; i < input.size(); i++)
    {
        for (int j = 1; j < input.at(0).size(); j++)
        {
            asteroids += check_direction(input, r, c, j, -i);
            asteroids += check_direction(input, r, c, -i, -j);
            asteroids += check_direction(input, r, c, i, j);
            asteroids += check_direction(input, r, c, -j, i);
        }
    }

    return asteroids;
}

template <typename T>
void print_map(std::vector<std::vector<T>> map)
{
    for (std::vector<T> i : map)
    {
        for (T j : i)
        {
            std::cout << j << " ";
        }
        std::cout << "\n";
    }
    std::cout << "------------------------ \n";
}

std::tuple<int, int> part1(std::vector<std::vector<int>> &input)
{
    // 286 solution
    int best_x = 0;
    int best_y = 0;
    int ast_max = 0;
    std::vector<std::vector<int>> visible_map(input.size(), std::vector<int>(input.at(0).size()));
    for (int i = 0; i < input.size(); i++)
    {
        for (int j = 0; j < input.at(0).size(); j++)
        {
            visible_map[i][j] = count_asteroids(input, i, j);
            if (visible_map[i][j] > ast_max)
            {
                ast_max = visible_map[i][j];
                best_x = i;
                best_y = j;
            }
        }
    }

    // print_map(visible_map);
    std::cout << "Best Station Count: " << ast_max << "\n";
    return std::make_tuple(best_x, best_y);
}

void calculate_angles(std::vector<std::vector<int>> input, int r, int c, std::map<int, std::vector<t_point>, std::greater<int>> &laser_angles)
{
    for (int i = 0; i < input.size(); i++)
    {
        for (int j = 0; j < input.at(0).size(); j++)
        {
            if (!input.at(i).at(j))
                continue;
            int angle = atan2(j - c, i - r) * 1e8; // make a large integer for comparison
            if (laser_angles.contains(angle))
            {
                laser_angles[angle].push_back({i, j});
            }
            else
            {
                std::vector<t_point> v = {t_point(i, j)};
                laser_angles.insert(std::pair{angle, v});
            }
        }
    }
}

t_point get_closest_asteroid(int idx, std::vector<t_point> asteroid_list, int r, int c)
{
    int best_dist = INT16_MAX;
    t_point best_p;
    for (auto a : asteroid_list)
    {
        int dist = (a.x - r) * (a.x - r) + (a.y - c) * (a.y - c);
        if (dist < best_dist)
        {
            best_dist = dist;
            best_p = a;
        }
    }
    // pop best point?
    return best_p;
}

void part2(std::vector<std::vector<int>> input, int r, int c)
{
    // solution 5 4 --> 504
    /**
     * Fill in every asteroid into a map (of lists) ordered by its angle to UP
     * Read out the closest asteroid in descending order & stop a Nr 200
     */
    std::map<int, std::vector<t_point>, std::greater<int>> laser_angles;
    calculate_angles(input, r, c, laser_angles);
    int idx = 0;
    for (auto asteroids : laser_angles)
    {
        t_point p = get_closest_asteroid(idx++, std::get<1>(asteroids), r, c);
        // std::cout << idx << " -- " << p.y << " " << p.x << "\n";
        if (idx == 200)
        {
            std::cout << "200st Asteroid: " << p.y << " " << p.x << "\n";
            break;
        }
    }
}

int main()
{
    std::ifstream inputFile("../10/input.txt");
    // std::ifstream inputFile("../10/example1.txt");
    // std::ifstream inputFile("../10/example2.txt");

    // input container
    std::vector<std::vector<int>> input;

    // ----------------------------------------------
    // Parse input to vector
    std::string line;
    while (std::getline(inputFile, line))
    {
        input.push_back(std::vector<int>());

        for (char c : line)
        {
            input.at(input.size() - 1).push_back(c == '#' ? 1 : 0);
        }
    }
    std::cout << "Loaded Map with size " << input.size() << "x" << input.at(0).size() << "\n";
    inputFile.close();

    // print_map(input);

    auto coords = part1(input);
    std::cout << "Best Location: " << std::get<1>(coords) << " - " << std::get<0>(coords) << "\n"; // Swap x-y for exercise output
    part2(input, std::get<0>(coords), std::get<1>(coords));
    return 0;
}