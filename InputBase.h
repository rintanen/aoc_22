#ifndef INPUTBASE_H
#define INPUTBASE_H

#include <iostream>

class InputBase
{
    private:
        
    public:
        InputBase(std::string str_input_path);
        ~InputBase();

        std::string str_input_path;

        std::string read_raw_input();  
};
#endif //INPUTBASE_H