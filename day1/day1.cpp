#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>


int main()
{   
    std::ifstream raw_input("input.txt");
    std::vector<uint32_t> calories;
    std::string line;

    uint32_t this_elf_calories = 0;
    while(getline(raw_input, line))
    {   
        if (line == "")
        {
            calories.push_back(this_elf_calories);
            this_elf_calories = 0;
            continue;
        }
        else this_elf_calories += stoi(line);
    }
    
    uint32_t max_calories = *std::max_element(calories.begin(), calories.end());

    std::cout << "PART 1: " << max_calories << std::endl;

    std::sort(calories.begin(), calories.end());

    std::vector<uint32_t> top_three(calories.end() - 3, calories.end());

    uint32_t top_three_sum = 0;
    for (int item: top_three)
    {
        top_three_sum += item;
    }

    std::cout << "PART 2: " << top_three_sum << std::endl;

    raw_input.close();
    
    return 0;
}
