package main

import (
	"fmt"
	"readline"
	"regexp"
	"strconv"
)

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func part1() {
	lines := readline.Readlines("input.txt")
	rows := len(lines)
	cols := len(lines[0])
	symbolRegex := regexp.MustCompile(`[^\d\.]`)
	totalPartNumbers := 0
	for currentRow, line := range lines {
		re := regexp.MustCompile(`\d+`)
		matches := re.FindAllStringIndex(line, -1)
		for _, match := range matches {
			isAdjacent := false
			start := match[0]
			end := match[1]
			for col := max(start-1, 0); col < min(end+1, cols); col++ {
				if symbolRegex.MatchString(string(lines[max(currentRow-1, 0)][col])) || symbolRegex.MatchString(string(lines[min(currentRow+1, rows-1)][col])) {
					isAdjacent = true
				}
			}
			if symbolRegex.MatchString(string(line[max(start-1, 0)])) || symbolRegex.MatchString(string(line[min(end, cols-1)])) {
				isAdjacent = true
			}
			if isAdjacent {
				val, _ := strconv.Atoi(line[start:end])
				totalPartNumbers += val
			}

		}
	}
	fmt.Printf("%d\n", totalPartNumbers)
}

func part2() {
	lines := readline.Readlines("input.txt")
	rows := len(lines)
	cols := len(lines[0])
	gearRegex := regexp.MustCompile(`\*`)
	gearMap := map[string][]int{}
	for currentRow, line := range lines {
		re := regexp.MustCompile(`\d+`)
		matches := re.FindAllStringIndex(line, -1)
		for _, match := range matches {
			gearLocation := [2]int{-1, -1}
			start := match[0]
			end := match[1]
			for col := max(start-1, 0); col < min(end+1, cols); col++ {
				if gearRegex.MatchString(string(lines[max(currentRow-1, 0)][col])) {
					gearLocation = [2]int{max(currentRow-1, 0), col}
				}
				if gearRegex.MatchString(string(lines[min(currentRow+1, rows-1)][col])) {
					gearLocation = [2]int{min(currentRow+1, rows-1), col}
				}
			}
			if gearRegex.MatchString(string(line[max(start-1, 0)])) {
				gearLocation = [2]int{currentRow, max(start-1, 0)}
			}
			if gearRegex.MatchString(string(line[min(end, cols-1)])) {
				gearLocation = [2]int{currentRow, min(end, cols-1)}
			}
			if gearLocation[0] != -1 {
				val, _ := strconv.Atoi(line[start:end])
				key := fmt.Sprintf("%d,%d", gearLocation[0], gearLocation[1])
				gearMap[key] = append(gearMap[key], val)
			}

		}
	}
	total := 0
	for _, parts := range gearMap {
		if len(parts) == 2 {
			total += parts[0] * parts[1]
		}
	}
	fmt.Printf("%d\n", total)
}

func main() {
	//part1()
	part2()
}
