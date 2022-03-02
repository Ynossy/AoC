#include <fstream>
#include <iostream>

int main()
{
    std::ifstream inputFile("../1/input.txt");
    int c;
    int fuel = 0;
    int fuelB = 0;
    while (inputFile >> c)
    {
        int mass = c / 3 - 2;
        fuel += mass;
        while (mass >= 0)
        {
            fuelB += mass;
            mass = mass / 3 - 2;
        }
    }
    std::cout << "P1: Fuel Needed: " << fuel;
    std::cout << " P2: Fuel Needed: " << fuelB;

    return 0;
}