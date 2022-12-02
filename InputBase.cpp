#include <iostream>
#include <fstream>

#include "InputBase.h"


InputBase::InputBase(std::string input) 
{
    str_input_path = input;
}

InputBase::~InputBase()
{
}

std::string InputBase::read_raw_input() 
{
    std::ifstream ifs(str_input_path);
    std::string raw_content((std::istreambuf_iterator<char>(ifs)),
                            (std::istreambuf_iterator<char>()));

    return raw_content;
}

int main()
{
    InputBase task_input("day1/input.txt");

    std::string raw_input = task_input.read_raw_input();
    
    int item_start = 0; 
    for (int i = 0; i<raw_input.length(); i++)
    {   
        if (&raw_input[i] == "\n")
        {
            std::cout << "lol" << "n";
        }


        
        // std::cout << raw_input[i] << "\n";
    }

    
    return 0;
}