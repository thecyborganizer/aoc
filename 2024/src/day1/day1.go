package main

import (
	"fmt"
	"input"
	"math"
	"readline"
	"slices"
)

func main() {
	input.GetInputForYearAndDay(2024, 1)
	lines := readline.Readlines("input.txt")
	left := []int{}
	right := []int{}
	for _, line := range lines {
		nums := readline.GetAllNumbers(line)
		left = append(left, nums[0])
		right = append(right, nums[1])
	}
	slices.Sort(left)
	slices.Sort(right)
	diff := 0
	for i, l := range left {
		diff += int(math.Abs(float64(l) - float64(right[i])))
	}
	fmt.Printf("part1: %d\n", diff)

	score := 0
	for _, l := range left {
		count := 0
		for _, r := range right {
			if l == r {
				count += 1
			}
		}
		score += l * count
	}
	fmt.Printf("part2: %d\n", score)
}
