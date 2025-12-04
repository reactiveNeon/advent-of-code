CXX = g++
CXXFLAGS = -std=c++23 -Wall -Wextra -O2

.PHONY: all clean part1 part2 test test1 test2

all: part1 part2

part1: part1.cpp
	$(CXX) $(CXXFLAGS) -o part1 part1.cpp

part2: part2.cpp
	$(CXX) $(CXXFLAGS) -o part2 part2.cpp

test1: part1.cpp
	$(CXX) $(CXXFLAGS) -DTEST_MODE -o test_part1 part1.cpp
	./test_part1

test2: part2.cpp
	$(CXX) $(CXXFLAGS) -DTEST_MODE -o test_part2 part2.cpp
	./test_part2

test: test1 test2

clean:
	rm -f part1 part2 test_part1 test_part2
