#include <iostream>

void step(int moons[4][6])
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = i + 1; j < 4; j++)
        {
            for (int k = 0; k < 3; k++)
            {
                if (moons[i][k] == moons[j][k])
                    continue;
                int gravity = (moons[i][k] > moons[j][k]) * 2 - 1;
                moons[i][k + 3] -= gravity;
                moons[j][k + 3] += gravity;
            }
        }
    }

    for (int i = 0; i < 4; i++)
    {
        for (int k = 0; k < 3; k++)
        {
            moons[i][k] += moons[i][k + 3];
        }
    }
}

void part1(int moons[4][6])
{
    // 3306 too low
    // 7098 right
    for (int i = 0; i < 1000; i++)
        step(moons);

    int energy = 0;
    for (int i = 0; i < 4; i++)
    {
        int potential = 0;
        int kinetic = 0;
        for (int k = 0; k < 3; k++)
        {
            potential += abs(moons[i][k]);
            kinetic += abs(moons[i][k + 3]);
            std::cout << moons[i][k] << " ";
        }
        energy += potential * kinetic;
        std::cout << "\n";
    }
    std::cout << "Total Energy: " << energy << "\n";
}

int main()
{
    // Skip Parsing
    /*
    <x=6, y=-2, z=-7>
    <x=-6, y=-7, z=-4>
    <x=-9, y=11, z=0>
    <x=-3, y=-4, z=6>
     */

    int moons[4][6] = {{6, -2, -7, 0, 0, 0},
                       {-6, -7, -4, 0, 0, 0},
                       {-9, 11, 0, 0, 0, 0},
                       {-3, -4, 6, 0, 0, 0}};

    /* Example:
    <x=-1, y=0, z=2>
    <x=2, y=-10, z=-7>
    <x=4, y=-8, z=8>
    <x=3, y=5, z=-1>
    */
    int example[4][6] = {{-1, 0, 2, 0, 0, 0},
                         {2, -10, -7, 0, 0, 0},
                         {4, -8, 8, 0, 0, 0},
                         {3, 5, -1, 0, 0, 0}};

    /* Example 2
    <x=-8, y=-10, z=0>
    <x=5, y=5, z=10>
    <x=2, y=-7, z=3>
    <x=9, y=-8, z=-3>
    */
    int example2[4][6] = {{-8, -10, 0, 0, 0, 0},
                         {5, 5, 10, 0, 0, 0},
                         {2, -7, 3, 0, 0, 0},
                         {9, -8, -3, 0, 0, 0}};

    part1(moons);
    return 0;
}