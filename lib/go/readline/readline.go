package readline

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func Readlines(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var output []string
	for scanner.Scan() {
		output = append(output, strings.TrimSpace(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return output
}

func ConvertToGrid(lines []string) [][]string {
	var grid [][]string
	for _, l := range lines {
		var row []string
		for _, r := range l {
			row = append(row, string(r))
		}
		grid = append(grid, row)
	}
	return grid
}

func GetAllNumbers(s string) []int {
	re := regexp.MustCompile(`-?\d+`)
	matches := re.FindAllString(s, -1)
	var numbers []int
	for _, match := range matches {
		val, _ := strconv.Atoi(match)
		numbers = append(numbers, val)
	}
	return numbers
}
