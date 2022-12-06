#include <iostream>
#include <string>
#include <fstream>
#include <map>


std::map<std::string, std::string> win_mp_pt1 =
{
    {"X", "C"},
    {"Y", "A"},
    {"Z", "B"}
};


std::map<std::string, std::string> lose_mp_pt1 =
{
    {"X", "B"},
    {"Y", "C"},
    {"Z", "A"}
};

std::map<std::string, std::string> win_mp_pt2 =
{
    {"A", "C"},
    {"B", "A"},
    {"C", "B"}
};

std::map<std::string, std::string> lose_mp_pt2 =
{
    {"A", "B"},
    {"B", "C"},
    {"C", "A"}
};


int outcome(std::string opponent_plays, std::string i_play)
{
    for (std::map<std::string, std::string>::iterator iter = win_mp_pt1.begin(); iter != win_mp_pt1.end(); iter++)
        if ((opponent_plays == iter->second) && (i_play == iter->first)) return 2;
    
    for (std::map<std::string, std::string>::iterator iter = lose_mp_pt1.begin(); iter != lose_mp_pt1.end(); iter++)
        if ((opponent_plays == iter->second) && (i_play == iter->first)) return 0;

    return 1;
}


int extra_points(std::string character)
{   
    int points;
    if (character == "X" || character == "A")
        points = 1;
    else if (character == "Y" || character == "B")
        points = 2;
    else if (character == "Z" || character == "C")
        points = 3;

    return points;
}


std::string wins(std::string opponent_plays)
{
    for (std::map<std::string, std::string>::iterator iter = lose_mp_pt2.begin(); iter != lose_mp_pt2.end(); iter++)
        if (opponent_plays == iter->first) return iter->second;
    return "";
}


std::string loses_to(std::string opponent_plays)
{
    for (std::map<std::string, std::string>::iterator iter = win_mp_pt2.begin(); iter != win_mp_pt2.end(); iter++)
        if (opponent_plays == iter->first) return iter->second;
    return "";
}


int main()
{
    std::ifstream raw_input("input.txt");
    std::string line;
    int points_from_outcome[] = {0, 3, 6};

    uint32_t points = 0;
    uint32_t points_pt2 = 0;
    while (getline(raw_input, line))
    {   
        std::string opponent_plays = line.substr(0, 1);
        std::string i_play = line.substr(2, 1);
        
        // PT1
        points += points_from_outcome[outcome(opponent_plays, i_play)];
        points += extra_points(i_play);

        // PT2
        if (i_play == "X") // lose
            i_play = loses_to(opponent_plays);
        else if (i_play == "Y") // draw
        {
            i_play = opponent_plays;
            points_pt2 += 3;
        } 
        else if (i_play == "Z") // win
        {
            i_play = wins(opponent_plays);
            points_pt2 += 6;
        } 

        points_pt2 += extra_points(i_play);
    }
    std::cout << "PART 1: " << points << std::endl;
    std::cout << "PART 2 " << points_pt2 << std::endl;
    
    raw_input.close();

    return 0;
}
