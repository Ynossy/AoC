#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

void task1(std::vector<int> input)
{
    // Wrong: 1596
    // Right: 1441
    // The image you received is 25 pixels wide and 6 pixels tall.
    const int w = 25;
    const int h = 6;

    int counter[3] = {0, 0, 0};
    int layer = 0;
    int max_layer = -1;
    int layer_count = INT32_MAX;
    int pixelcounter = w * h;
    for (int d : input)
    {
        counter[d]++;
        pixelcounter--;
        if (pixelcounter == 0)
        {
            pixelcounter = w * h;
            if (counter[0] < layer_count)
            {
                layer_count = counter[0];
                max_layer = layer;
                std::cout << "New best Layer: " << max_layer << " --- " << counter[0] << " --- Res: " << counter[1] * counter[2] << "\n";
            }
            counter[0] = 0;
            counter[1] = 0;
            counter[2] = 0;
            layer++;
        }
    }
}

void task2(std::vector<int> input)
{
    // RUZBP
    // ###__#__#_####_###__###__
    // #__#_#__#____#_#__#_#__#_
    // #__#_#__#___#__###__#__#_
    // ###__#__#__#___#__#_###__
    // #_#__#__#_#____#__#_#____
    // #__#__##__####_###__#____
    const int w = 25;
    const int h = 6;
    int image[w * h];
    std::fill_n(image, w * h, 2);

    int pixel_idx = 0;

    for (int i : input)
    {
        if (image[pixel_idx] == 2)
        {
            image[pixel_idx] = i;
        }
        pixel_idx = (pixel_idx + 1) % (w * h);
    }

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (image[i * w + j] == 0)
            {
                std::cout << '_';
            }
            else
            {
                std::cout << '#';
            }
        }
        std::cout << "\n";
    }
}

int main()
{
    std::ifstream inputFile("../8/input.txt");

    // input container
    std::vector<int> input;

    // ----------------------------------------------
    // Parse input to vector
    std::string line;
    std::getline(inputFile, line);
    for (char &c : line)
    {
        input.push_back((int)c - (int)'0');
    }
    inputFile.close();

    task1(input);
    task2(input);
    return 0;
}