package main

import (
	"fmt"
	"input"
	"math"
	"readline"
	"regexp"
	"slices"
	"strconv"
)

func findMaxIndex(s []int) int {
	max := 0
	index := -1
	for i, n := range s {
		if n > max {
			index = i
			max = n
		}
	}
	return index
}

func twoBatteryJoltage(s []int) int {
	tensBatteryIndex := findMaxIndex(s[:len(s)-1])
	onesBatteryIndex := findMaxIndex(s[tensBatteryIndex+1:])
	joltage := 10*s[tensBatteryIndex] + s[tensBatteryIndex+onesBatteryIndex+1]
	return joltage
}

func twelveBatteryJoltage(s []int) int {
	fmt.Printf("%v\n", s)
	start := 0
	end := len(s) - 11
	extra := len(s) - 11
	var batteriesToUse []int
	total := 0
	var indices []int
	for i := 0; i < 12; i++ {
		index := findMaxIndex(s[start:end])
		batteriesToUse = append(batteriesToUse, s[start+index])
		indices = append(indices, start+index)
		start = start + index + 1
		extra = extra - index
		end = start + extra
	}
	fmt.Printf("[")
	for i, v := range s {
		match := false
		for _, b := range indices {
			if b == i {
				match = true
				fmt.Printf("%d", v)
			}
		}
		if !match {
			fmt.Printf("_")
		}
		if i != len(s)-1 {
			fmt.Printf(" ")
		}
	}
	fmt.Printf("]\n")
	slices.Reverse(batteriesToUse)
	for i, v := range batteriesToUse {
		exp := int(math.Pow10(i))
		total += (v * exp)
	}
	return total
}

func main() {
	input.GetInputForYearAndDay(2025, 3)
	lines := readline.Readlines("input.txt")
	//lines := readline.Readlines("test.txt")
	partOneTotal := 0
	partTwoTotal := 0
	re := regexp.MustCompile(`\d`)
	for _, l := range lines {
		var batteries []int
		for _, c := range re.FindAllString(l, -1) {
			n, _ := strconv.Atoi(c)
			batteries = append(batteries, n)
		}
		partOneTotal += twoBatteryJoltage(batteries)
		partTwoTotal += twelveBatteryJoltage(batteries)
	}
	fmt.Printf("part1: %d\n", partOneTotal)
	fmt.Printf("part2: %d\n", partTwoTotal)

}
