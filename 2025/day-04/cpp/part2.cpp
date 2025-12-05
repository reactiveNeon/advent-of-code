#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int solve(const std::string &input_path) {
    using namespace std;
    
    std::ifstream file(input_path);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + input_path);
    }
    
    vector<vector<char>> grid;

    std::string line;
    while (std::getline(file, line)) {
        vector<char> row(line.begin(), line.end());
        grid.push_back(row);
    }
    
    auto in_bounds = [&grid](int j, int i) -> bool {
        return j >= 0 and j < grid.size() and i >= 0 and i < grid.front().size();
    };
    vector<pair<int, int>> dirs {{-1, -1}, {-1, 1}, {-1, 0}, {1, -1}, {1, 1}, {1, 0}, {0, -1}, {0, 1}};
    
    int removed = 0;
    
    vector<pair<int, int>> to_remove;
    do {        
        to_remove.clear();
        
        for(int j = 0; j < grid.size(); j++) {
            for(int i = 0; i < grid.front().size(); i++) {
                if(grid[j][i] == '.') {
                    continue;
                }
                
                int count = 0;
                
                for(auto [dy, dx] : dirs) {
                    int ny = dy + j, nx = dx + i;
                    
                    if(not in_bounds(ny, nx)) {
                        continue;
                    }
                    
                    if(grid[ny][nx] == '@') {
                        count++;
                    }
                }
                
                if(count < 4) {
                    removed++;
                    to_remove.push_back({j, i});
                }
            }
        }
        
        for(auto [j, i] : to_remove) {
            grid[j][i] = '.';
        }
    } while(not to_remove.empty());
    
    return removed;
}

#ifndef TEST_MODE
int main() {
    try {
        auto start = std::chrono::high_resolution_clock::now();
        int result = solve("inputs/input.txt");
        auto end = std::chrono::high_resolution_clock::now();
        auto elapsed =
            std::chrono::duration_cast<std::chrono::milliseconds>(end - start)
                .count();
        std::cout << result << std::endl;
        std::cerr << "\033[36mRuntime: " << elapsed << "ms\033[0m" << std::endl;
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
#endif

#ifdef TEST_MODE
#include <cassert>

void test_part2() {
    int expected = 0;  // TODO: Set expected result
    int result = solve("inputs/test.txt");
    if (result != expected) {
        std::cout << "\033[31mTest failed! Expected " << expected << " but got "
                  << result << "\033[0m" << std::endl;
        return;
    }
    std::cout << "\033[32mTest passed!\033[0m" << std::endl;
}

int main() {
    test_part2();
    return 0;
}
#endif
