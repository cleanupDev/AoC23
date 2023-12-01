package solutions

import (
	"path/filepath"

	"github.com/cleanupDev/AoC23/Day1/Go/internal"
)

var digitMap = map[string]string{
	"one":   "1",
	"two":   "2",
	"three": "3",
	"four":  "4",
	"five":  "5",
	"six":   "6",
	"seven": "7",
	"eight": "8",
	"nine":  "9",
}

func Part2() int {
	// File
	var inputFile = filepath.Join("../data/", "input.txt")
	path, _ := filepath.Abs(inputFile)

	// Read input
	data, err := internal.ReadInput(path)
	if err != nil {
		panic(err)
	}

	// apply digit map
	data = internal.ConvertDataToDigitMap(data, digitMap)

	// main logic
	sum, err := internal.GetSumOfDoubleDigit(data)
	if err != nil {
		panic(err)
	}

	return sum

}
