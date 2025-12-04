#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int solve(const std::string &input_path)
{
    std::ifstream file(input_path);
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file: " + input_path);
    }

    std::string line;
    while (std::getline(file, line))
    {
        // TODO: Implement solution
    }

    return 0;
}

#ifndef TEST_MODE
int main()
{
    try
    {
        int result = solve("inputs/input1.txt");
        std::cout << result << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
#endif

#ifdef TEST_MODE
#include <cassert>

void test_part1()
{
    int expected = 0; // TODO: Set expected result
    int result = solve("inputs/test1.txt");
    assert(result == expected && "Test failed!");
    std::cout << "Test passed!" << std::endl;
}

int main()
{
    test_part1();
    return 0;
}
#endif
