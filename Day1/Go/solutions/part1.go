package solutions

import (
	"path/filepath"

	"github.com/cleanupDev/AoC23/Day1/Go/internal"
)

func Part1() int {
	// File
	var inputFile = filepath.Join("../data/", "input.txt")
	path, _ := filepath.Abs(inputFile)

	// Read input
	data, err := internal.ReadInput(path)
	if err != nil {
		panic(err)
	}

	// main logic
	sum, err := internal.GetSumOfDoubleDigit(data)
	if err != nil {
		panic(err)
	}

	return sum
}
