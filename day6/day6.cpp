#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>


int n_unique(std::string str)
{
    std::set<char> str_unique_values(str.begin(), str.end());
    int num_unique = str.length() - (str.length() - str_unique_values.size());
    return num_unique;
}

class DataStreamBuffer
{
private:
    std::string buffer;
    int start_of_marker(int num_distinc_chars);
public:
    DataStreamBuffer(std::string buffer);
    ~DataStreamBuffer();
    int start_of_packet_marker();
    int start_of_message_marker();
};

DataStreamBuffer::DataStreamBuffer(std::string buffer)
{
    this->buffer = buffer;
}

DataStreamBuffer::~DataStreamBuffer(){}

int DataStreamBuffer::start_of_packet_marker()
{
    return this->start_of_marker(4);
}


int DataStreamBuffer::start_of_message_marker()
{
    return this->start_of_marker(14);
}

int DataStreamBuffer::start_of_marker(int num_distinc_chars)
{   
    for (int i = num_distinc_chars; i < this->buffer.length(); i++)
    {
        if (n_unique(this->buffer.substr(i - num_distinc_chars, num_distinc_chars)) == num_distinc_chars)
            return i;
    }
    return 0;    
}

int main()
{   
    std::ifstream filestream("input.txt");
    std::string task_input;
    std::getline(filestream, task_input);
    DataStreamBuffer dsb(task_input);

    std::cout << "PART 1: " << dsb.start_of_packet_marker() << std::endl;
    std::cout << "PART 2: " << dsb.start_of_message_marker() << std::endl;

    filestream.close();
    return 0;
}