package main

import (
	"fmt"
	"input"
	"readline"
	"slices"
	"strconv"
	"strings"
)

func main() {
	input.GetInputForYearAndDay(2025, 5)
	lines := readline.Readlines("input.txt")
	//lines := readline.Readlines("test.txt")
	var ranges [][]int
	var ingredients []int
	for _, l := range lines {
		if strings.Contains(l, "-") {
			thisRange := readline.GetAllNumbers(l)
			thisRange[1] *= -1
			ranges = append(ranges, thisRange)
		} else if len(l) > 0 {
			v, _ := strconv.Atoi(l)
			ingredients = append(ingredients, v)
		}
	}
	fresh := 0
	for _, ingredient := range ingredients {
	found:
		for _, freshRange := range ranges {
			if ingredient >= freshRange[0] && ingredient <= freshRange[1] {
				fresh++
				break found
			}
		}
	}

	slices.SortFunc(ranges, func(r1 []int, r2 []int) int {
		if r1[0] < r2[0] {
			return -1
		}
		if r1[0] > r2[0] {
			return 1
		}
		return 0
	})
	var merged [][]int

	for i := 0; i < len(ranges)-1; {
		if ranges[i][1]+1 < ranges[i+1][0] {
			merged = append(merged, ranges[i])
			i++
		} else {
			var newRange []int
			if ranges[i][1] < ranges[i+1][1] {
				newRange = []int{ranges[i][0], ranges[i+1][1]}
			} else {
				newRange = []int{ranges[i][0], ranges[i][1]}
			}
			ranges = slices.Delete(ranges, i, i+2)
			ranges = slices.Insert(ranges, i, newRange)
		}
	}
	merged = append(merged, ranges[len(ranges)-1])
	total := 0
	fmt.Printf("%v\n", merged)
	for _, m := range merged {
		toAdd := (m[1] - m[0]) + 1
		fmt.Printf("%d\n", toAdd)
		total += toAdd
	}

	fmt.Printf("part1: %d\n", fresh)
	fmt.Printf("part2: %d\n", total)
}
