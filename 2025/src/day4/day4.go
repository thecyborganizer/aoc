package main

import (
	"fmt"
	"input"
	"readline"
)

func printGrid(grid [][]string) {
	for y, row := range grid {
		for x, r := range row {
			if (r) == "@" {
				if isAccessible(grid, x, y) {
					fmt.Printf("x")
				} else {
					fmt.Printf("%s", r)
				}
			} else {
				fmt.Printf("%s", r)
			}
		}
		fmt.Printf("\n")
	}
}

func isAccessible(grid [][]string, x int, y int) bool {
	adjacencies := 0
	if y > 0 {
		// NW
		if x > 0 && (grid[y-1][x-1]) == "@" {
			adjacencies++
		}
		// N
		if (grid[y-1][x]) == "@" {
			adjacencies++
		}
		// NE
		if x < len(grid[y])-1 && (grid[y-1][x+1]) == "@" {
			adjacencies++
		}
	}
	// E
	if x < len(grid[y])-1 && (grid[y][x+1]) == "@" {
		adjacencies++
	}
	if y < len(grid)-1 {
		// SE
		if x < len(grid[y])-1 && (grid[y+1][x+1]) == "@" {
			adjacencies++
		}
		// S
		if (grid[y+1][x]) == "@" {
			adjacencies++
		}
		// SW
		if x > 0 && (grid[y+1][x-1]) == "@" {
			adjacencies++
		}
	}
	// W
	if x > 0 && (grid[y][x-1]) == "@" {
		adjacencies++
	}

	return adjacencies < 4
}

func main() {
	input.GetInputForYearAndDay(2025, 4)
	lines := readline.Readlines("input.txt")
	//lines := readline.Readlines("test.txt")
	var grid [][]string
	for _, l := range lines {
		var row []string
		for _, r := range l {
			row = append(row, string(r))
		}
		grid = append(grid, row)
	}
	accessible := 0
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			if (grid[y][x]) == "@" && isAccessible(grid, x, y) {
				accessible++
			}
		}
	}
	//printGrid(grid)
	var toRemove [][]int
	moreToRemove := true
	removed := 0
	for moreToRemove {
		for y := 0; y < len(grid); y++ {
			for x := 0; x < len(grid[0]); x++ {
				if (grid[y][x]) == "@" && isAccessible(grid, x, y) {
					toRemove = append(toRemove, []int{x, y})
				}
			}
		}
		removed += len(toRemove)
		fmt.Printf("removing %d\n", len(toRemove))
		for _, coordinateToRemove := range toRemove {
			x := coordinateToRemove[0]
			y := coordinateToRemove[1]
			grid[y][x] = "."
		}
		printGrid(grid)
		if len(toRemove) == 0 {
			moreToRemove = false
		}
		toRemove = [][]int{}
	}

	fmt.Printf("part1: %d\n", accessible)
	fmt.Printf("part2: %d\n", removed)
}
