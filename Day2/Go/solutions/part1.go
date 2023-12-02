package solutions

import (
	"fmt"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"

	"github.com/cleanupDev/AoC23/Day2/Go/internal"
)

func splitStrings(s string) []string {
	return strings.Split(s, ",")
}

func lineToItems(line string) []string {
	regex := regexp.MustCompile(`^Game \d{1,3}: `)
	line = regex.ReplaceAllString(line, "")
	line = strings.ReplaceAll(line, " ", "")
	lineItems := strings.Split(line, ";")
	return lineItems
}

func getSumLine(line []string) [][]int {
	regex := regexp.MustCompile(`\d{1,3}`)
	result := [][]int{}

	for _, cubeSet := range line {
		items := splitStrings(cubeSet)
		lineResult := []int{}
		for _, item := range items {
			numberString := regex.FindString(item)
			numberInt, _ := strconv.Atoi(numberString)

			switch {
			case strings.Contains(item, "red"):
				lineResult = append(lineResult, numberInt)

			case strings.Contains(item, "green"):
				lineResult = append(lineResult, numberInt)

			case strings.Contains(item, "blue"):
				lineResult = append(lineResult, numberInt)
			default:
				fmt.Println("Error on item: ", item)
				lineResult = append(lineResult, 0)

			}
		}

		if len(lineResult) < 3 {
			for i := len(lineResult); i < 3; i++ {
				lineResult = append(lineResult, 0)
			}
		}

		result = append(result, lineResult)
	}
	return result
}

func validateSet(set []int) bool {
	redLimit, greenLimit, blueLimit := 12, 13, 14
	return (set[0] <= redLimit) && (set[1] <= greenLimit) && (set[2] <= blueLimit)
}

func filterValidLine(line [][]int) bool {
	for _, set := range line {
		if !validateSet(set) {
			return false
		}
	}
	return true

}

func Part1() int {
	// File
	var inputFile = filepath.Join("../data/", "input.txt")
	path, _ := filepath.Abs(inputFile)

	// Read input
	data, err := internal.ReadInput(path)
	if err != nil {
		panic(err)
	}

	result := 0

	for i, line := range data {
		lineItems := lineToItems(line)
		lineResult := getSumLine(lineItems)
		if filterValidLine(lineResult) {
			result += i + 1
		}

	}

	return result
}
