package main

import (
	"fmt"
	"input"
	"output"
	"readline"
)

func xmasCount(grid [][]string, x int, y int) int {
	if grid[y][x] != "X" {
		return 0
	}
	count := 0
	if y >= 3 {
		// NW
		if x >= 3 && (grid[y-1][x-1]) == "M" && grid[y-2][x-2] == "A" && grid[y-3][x-3] == "S" {
			count++
		}
		// N
		if (grid[y-1][x]) == "M" && grid[y-2][x] == "A" && grid[y-3][x] == "S" {
			count++
		}
		// NE
		if x < len(grid[y])-3 && (grid[y-1][x+1]) == "M" && grid[y-2][x+2] == "A" && grid[y-3][x+3] == "S" {
			count++
		}
	}
	// E
	if x < len(grid[y])-3 && (grid[y][x+1]) == "M" && grid[y][x+2] == "A" && grid[y][x+3] == "S" {
		count++
	}
	if y < len(grid)-3 {
		// SE
		if x < len(grid[y])-3 && (grid[y+1][x+1]) == "M" && grid[y+2][x+2] == "A" && grid[y+3][x+3] == "S" {
			count++
		}
		// S
		if (grid[y+1][x]) == "M" && grid[y+2][x] == "A" && grid[y+3][x] == "S" {
			count++
		}
		// SW
		if x >= 3 && (grid[y+1][x-1]) == "M" && grid[y+2][x-2] == "A" && grid[y+3][x-3] == "S" {
			count++
		}
	}
	// W
	if x >= 3 && (grid[y][x-1]) == "M" && grid[y][x-2] == "A" && grid[y][x-3] == "S" {
		count++
	}

	return count
}

func pt2Count(grid [][]string, x int, y int) int {
	if grid[y][x] != "A" || x < 1 || y < 1 || x > len(grid[y])-2 || y > len(grid)-2 {
		return 0
	}
	count := 0
	if (grid[y-1][x-1] == "M" && grid[y+1][x+1] == "S") || (grid[y-1][x-1] == "S" && grid[y+1][x+1] == "M") {
		if (grid[y-1][x+1] == "M" && grid[y+1][x-1] == "S") || (grid[y-1][x+1] == "S" && grid[y+1][x-1] == "M") {
			count++
		}
	}
	return count
}

func main() {
	input.GetInputForYearAndDay(2024, 4)
	//grid := readline.ConvertToGrid(readline.Readlines("test.txt"))
	grid := readline.ConvertToGrid(readline.Readlines("input.txt"))
	output.PrintGrid(grid)
	total := 0
	pt2total := 0

	for y := range grid {
		for x := range grid[0] {
			total += xmasCount(grid, x, y)
			pt2total += pt2Count(grid, x, y)
		}
	}
	fmt.Printf("part1: %d\n", total)
	fmt.Printf("part2: %d\n", pt2total)
}
