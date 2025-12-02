package main

import (
	"fmt"
	"input"
	"readline"
	"slices"
)

func isLineSafe(nums []int) bool {
	direction := ""
	if nums[0] > nums[len(nums)-1] {
		direction = "down"
	} else if nums[0] < nums[len(nums)-1] {
		direction = "up"
	} else {
		return false
	}
	for i := 0; i < len(nums)-1; i++ {
		delta := 0
		if direction == "up" {
			delta = nums[i+1] - nums[i]
		} else {
			delta = nums[i] - nums[i+1]
		}
		if delta < 1 || delta > 3 {
			return false
		}
	}
	return true
}

func main() {
	input.GetInputForYearAndDay(2024, 2)
	lines := readline.Readlines("input.txt")
	//lines := readline.Readlines("test.txt")
	count := 0

	dampedCount := 0
	for _, line := range lines {
		fmt.Printf("%s: ", line)
		nums := readline.GetAllNumbers(line)
		safe := false
		removed := -1
		if isLineSafe(nums) {
			fmt.Println("safe without removing anything")
			count += 1
		} else {
			for skip := 0; skip < len(nums); skip++ {
				subset := slices.Clone(nums)
				subset = slices.Delete(subset, skip, skip+1)
				if isLineSafe(subset) {
					safe = true
					removed = skip
					skip = len(nums) - 1
				}
			}
			if safe {
				dampedCount++
				fmt.Printf("safe by removing %d (index %d)\n", nums[removed], removed)
			} else {
				fmt.Println("unsafe")
			}
		}
	}
	fmt.Printf("part1: %d\n", count)
	fmt.Printf("part2: %d\n", count+dampedCount)
}
