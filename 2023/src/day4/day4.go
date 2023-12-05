package main

import (
	"fmt"
	"math"
	"readline"
)

var winningNumbersEnd = 11

func part1() {
	lines := readline.Readlines("input.txt")
	totalScore := 0
	for _, line := range lines {
		numbers := readline.GetAllNumbers(line)
		winningNumbers := numbers[1:11]
		numbersIHave := numbers[11:]
		matches := 0
		for _, n := range numbersIHave {
			for _, w := range winningNumbers {
				if n == w {
					matches++
				}
			}
		}
		if matches > 0 {
			totalScore += int(math.Pow(float64(2), float64(matches-1)))
		}
	}
	fmt.Printf("%d\n", totalScore)
}

func part2() {
	lines := readline.Readlines("input.txt")
	numberOfCards := make([]int, len(lines))
	for i, _ := range numberOfCards {
		numberOfCards[i] = 1
	}
	for i, line := range lines {
		numbers := readline.GetAllNumbers(line)
		winningNumbers := numbers[1:winningNumbersEnd]
		numbersIHave := numbers[winningNumbersEnd:]
		numberOfCardsPastThisOneToDuplicate := 0
		for _, n := range numbersIHave {
			for _, w := range winningNumbers {
				if n == w {
					numberOfCardsPastThisOneToDuplicate++
				}
			}
		}
		numberOfTimesToDuplicate := numberOfCards[i]
		for j := i + 1; j < i+numberOfCardsPastThisOneToDuplicate+1; j++ {
			numberOfCards[j] += numberOfTimesToDuplicate
		}
	}
	totalCards := 0
	for _, c := range numberOfCards {
		totalCards += c
	}
	fmt.Printf("%d\n", totalCards)

}

func main() {
	//part1()
	part2()
}
