#include <iostream>
#include <fstream>

#include "../InputBase.h"

// class Input: InputBase
// {
//     public:
//         int read_task_input();
// };

// int Input::read_task_input()
// {
//     int items[50];
// }

int main()
{   
    InputBase task_input("input.txt");

    std::string raw_input = task_input.read_raw_input();

    std::cout << raw_input << "\n";
  
    return 0;
}