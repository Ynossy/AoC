#include <iostream>

/**
 * Greatest common divisor
 */
long gcd(long a, long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

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
            // std::cout << moons[i][k] << " ";
        }
        energy += potential * kinetic;
        // std::cout << "\n";
    }
    std::cout << "Total Energy: " << energy << "\n";
}

void part2(int moons[4][6])
{
    /**
     * x,y and z evolve independent --> find cycle length for each and get the least common multiple
     * Solution: 400128139852752
     */
    int init_pos[4][3];
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            init_pos[i][j] = moons[i][j];
        }
    }
    int x_cycle = 0;
    int y_cycle = 0;
    int z_cycle = 0;
    int cycle = 0;
    while (!x_cycle || !y_cycle || !z_cycle)
    {
        step(moons);
        cycle++;
        if(!x_cycle && moons[0][0]==init_pos[0][0] && moons[1][0]==init_pos[1][0] && moons[2][0]==init_pos[2][0] && moons[3][0]==init_pos[3][0]){
            x_cycle = cycle+1;
        }
        if(!y_cycle && moons[0][1]==init_pos[0][1] && moons[1][1]==init_pos[1][1] && moons[2][1]==init_pos[2][1] && moons[3][1]==init_pos[3][1]){
            y_cycle = cycle+1;
        }
        if(!z_cycle && moons[0][2]==init_pos[0][2] && moons[1][2]==init_pos[1][2] && moons[2][2]==init_pos[2][2] && moons[3][2]==init_pos[3][2]){
            z_cycle = cycle+1;
        }

        if(cycle > 1e6) break;
    }
    // std::cout << x_cycle << " " << y_cycle << " " << z_cycle << "\n";
    // long result = 0;
    // do
    // { // bruteforce lcm
    //     result += x_cycle; 
    // } while (result%y_cycle != 0 || result%z_cycle !=0);
    long p1 = gcd(x_cycle,y_cycle);
    long p2 = x_cycle/p1*y_cycle;
    long p3 = gcd(p2,z_cycle);
    long result = p2/p3*z_cycle;

    std::cout << "LCM: " << result << "\n";
    
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
    int moons2[4][6] = {{6, -2, -7, 0, 0, 0},
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
    part2(moons2);
    return 0;
}