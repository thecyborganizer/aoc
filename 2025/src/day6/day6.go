package main

import (
	"fmt"
	"input"
	"readline"
	"regexp"
	"strconv"
)

func main() {
	input.GetInputForYearAndDay(2025, 6)
	lines := readline.Readlines("input.txt")
	//lines := readline.Readlines("test.txt")
	var numbers [][]int
	for i := 0; i < len(lines)-1; i++ {
		numbers = append(numbers, readline.GetAllNumbers(lines[i]))
	}
	signsPattern := regexp.MustCompile(`[^\s]`)
	signs := signsPattern.FindAllString(lines[len(lines)-1], -1)
	grandTotal := 0
	for x := 0; x < len(numbers[0]); x++ {
		sign := signs[x]
		var total int
		if sign == "*" {
			total = 1
		}
		for y := 0; y < len(numbers); y++ {
			switch sign {
			case "+":
				total += numbers[y][x]
			case "*":
				total *= numbers[y][x]
			}
		}
		grandTotal += total
	}
	fmt.Printf("part1: %d\n", grandTotal)

	grid := readline.ConvertToGrid(lines)
	var moreNumbers []int
	var part2Total int
	for x := len(grid[0]) - 1; x >= 0; x-- {
		var number string
		var y int
		for y = 0; y < len(grid)-1; y++ {
			if grid[y][x] != " " && grid[y][x] != "x" {
				number = number + grid[y][x]
			}
		}
		if number != "" {
			val, _ := strconv.Atoi(number)
			moreNumbers = append(moreNumbers, val)
		}
		if y == len(grid)-1 && grid[y][x] != " " && grid[y][x] != "x" {
			sign := grid[y][x]
			fmt.Printf("%v %s\n", moreNumbers, sign)
			total := 0
			if sign == "*" {
				total = 1
			}
			for _, num := range moreNumbers {
				if sign == "+" {
					total += num
				} else {
					total *= num
				}
			}
			part2Total += total
			moreNumbers = []int{}
			y = 0
		}
	}
	fmt.Printf("part2: %d\n", part2Total)
}
