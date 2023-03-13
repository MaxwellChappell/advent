#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream file;
    std::string line;

    file.open("01.txt");

    while (std::getline(file, line))
    {
        std::cout << line << std::endl;
        if (line == "\n")
        {
            std::cout << "Here" << std::endl;
        }
    }

    file.close();
}