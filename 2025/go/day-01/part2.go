package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	result, err := solve("inputs/input2.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(result)
}

func solve(inputPath string) (int, error) {
	file, err := os.Open(inputPath)
	if err != nil {
		return 0, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	
	// TODO: Implement solution
	for scanner.Scan() {
		line := scanner.Text()
		_ = line
	}

	if err := scanner.Err(); err != nil {
		return 0, err
	}

	return 0, nil
}
