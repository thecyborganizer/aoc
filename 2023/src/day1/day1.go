package main

import (
	"fmt"
	"readline"
	"strconv"
	"strings"
)

func part1() {
	lines := readline.Readlines("input.txt")
	sum := 0
	for _, l := range lines {
		firstDigit := 0
		lastDigit := 0
		for _, c := range l {
			val, err := strconv.Atoi(string(c))
			if err == nil {
				firstDigit = val
				break
			}
		}
		for i := len(l) - 1; i >= 0; i-- {
			val, err := strconv.Atoi(string(l[i]))
			if err == nil {
				lastDigit = val
				break
			}
		}
		sum = sum + (firstDigit * 10) + lastDigit
	}

	fmt.Printf("%d\n", sum)
}

func isNumber(s string, i int, words []string, wordsMap map[string]int) (int, error) {
	val, err := strconv.Atoi(string(s[i]))
	if err == nil {
		return val, nil
	}
	for _, w := range words {
		if strings.HasPrefix(s[i:], w) {
			return wordsMap[w], nil
		}
	}
	return 0, fmt.Errorf("not a number")
}

func part2() {
	wordsMap := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
	words := make([]string, len(wordsMap))
	index := 0
	for k := range wordsMap {
		words[index] = k
		index++
	}
	sum := 0
	lines := readline.Readlines("input.txt")
	for _, l := range lines {
		firstDigit := 0
		lastDigit := 0
		for i, _ := range l {
			val, err := isNumber(l, i, words, wordsMap)
			if err == nil {
				firstDigit = val
				break
			}
		}
		for i := len(l) - 1; i >= 0; i-- {
			val, err := isNumber(l, i, words, wordsMap)
			if err == nil {
				lastDigit = val
				break
			}
		}
		fmt.Printf("%d\n", (firstDigit+10)+lastDigit)
		sum = sum + (firstDigit * 10) + lastDigit
	}
	fmt.Printf("%d\n", sum)
}

func main() {
	part1()
	part2()
}
