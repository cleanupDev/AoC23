package internal

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

func findFirstDigit(line string) (string, error) {
	// returns the first digit found in a string
	for _, char := range line {
		if unicode.IsDigit(char) {
			return string(char), nil
		}
	}
	return "", fmt.Errorf("no matching digits found")
}

func reverse(s string) string {
	// reverses a string
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func getLineDoubleDigit(line string) (int, error) {
	// concatenates the first and last digit of a string and returns the number
	firstDigit, err := findFirstDigit(line)
	if err != nil {
		return 0, err
	}
	lastDigit, err := findFirstDigit(reverse(line))
	if err != nil {
		return 0, err
	}

	number, err := strconv.Atoi(firstDigit + lastDigit)
	if err != nil {
		return 0, err
	}

	return number, nil
}

func GetSumOfDoubleDigit(data []string) (int, error) {
	// returns the sum of all double digits in a slice of strings
	var sum int

	for _, line := range data {
		number, err := getLineDoubleDigit(line)
		if err != nil {
			return 0, err
		}
		sum += number
	}

	return sum, nil
}

// ----- Part 2 -----

func applyDigitMapping(line string, mapping map[string]string) string {
	// applies the digit mapping to a single line
	for key, value := range mapping {
		if len(key) > 0 {
			firstChar := string(key[0])
			lastChar := string(key[len(key)-1])
			newValue := firstChar + value + lastChar
			line = strings.ReplaceAll(line, key, newValue)
		}
	}
	return line
}

func ConvertDataToDigitMap(data []string, mapping map[string]string) []string {
	// applies the digit mapping to a slice of strings
	var convertedData []string
	for _, line := range data {
		convertedData = append(convertedData, applyDigitMapping(line, mapping))
	}
	return convertedData
}
