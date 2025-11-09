package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	expected := 0 // TODO: Set expected result
	result, err := solve("inputs/test1.txt")
	if err != nil {
		t.Fatalf("Error solving: %v", err)
	}
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}
