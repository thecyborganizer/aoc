package main

import (
	"fmt"
	"input"
	"readline"
	"regexp"
	"strconv"
	"strings"
)

func getMulFromString(s string) int {
	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	matches := re.FindAllStringSubmatch(s, -1)
	total := 0
	for _, match := range matches {
		lval, _ := strconv.Atoi(match[1])
		rval, _ := strconv.Atoi(match[2])
		total += lval * rval
	}
	return total

}

func main() {
	input.GetInputForYearAndDay(2024, 3)
	line := strings.Join(readline.Readlines("input.txt"), "")
	//line := "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
	total := getMulFromString(line)
	fmt.Printf("part1: %d\n", total)

	state := "do"
	doPattern := regexp.MustCompile(`do\(\)`)
	dontPattern := regexp.MustCompile(`don't\(\)`)
	total = 0
	for index := 0; index < len(line); {
		switch state {
		case "do":
			nextIndexResult := dontPattern.FindStringIndex(line[index:])
			if nextIndexResult != nil {
				nextIndex := nextIndexResult[1]
				total += getMulFromString(line[index : index+nextIndex])
				state = "don't"
				index += nextIndex
			} else {
				total += getMulFromString(line[index:])
				index = len(line)
			}
		case "don't":
			nextIndexResult := doPattern.FindStringIndex(line[index:])
			if nextIndexResult != nil {
				nextIndex := nextIndexResult[1]
				state = "do"
				index += nextIndex
			} else {
				index = len(line)
			}
		}
	}
	fmt.Printf("part2: %d\n", total)
}
