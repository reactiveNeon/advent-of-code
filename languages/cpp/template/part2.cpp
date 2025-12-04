#include <chrono>
#include <fstream>
#include <iostream>
#include <string>

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
        auto start = std::chrono::high_resolution_clock::now();
        int result = solve("inputs/input.txt");
        auto end = std::chrono::high_resolution_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
        std::cout << result << std::endl;
        std::cerr << "\033[36mRuntime: " << elapsed << "ms\033[0m" << std::endl;
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

void test_part2()
{
    int expected = 0; // TODO: Set expected result
    int result = solve("inputs/test.txt");
    if (result != expected)
    {
        std::cout << "\033[31mTest failed! Expected " << expected << " but got " << result << "\033[0m" << std::endl;
        return;
    }
    std::cout << "\033[32mTest passed!\033[0m" << std::endl;
}

int main()
{
    test_part2();
    return 0;
}
#endif
