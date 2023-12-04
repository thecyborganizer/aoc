package main

import (
	"fmt"
	"readline"
	"regexp"
	"strconv"
	"strings"
)

func matchOrReturnZero(s string, color string) int {
	re := regexp.MustCompile(`(\d+) ` + color)
	match := re.FindStringSubmatch(s)
	if match == nil {
		return 0
	}
	val, _ := strconv.Atoi(match[1])
	return val
}

// red, green, blue
func countMarbles(s string) (int, int, int) {
	return matchOrReturnZero(s, "red"), matchOrReturnZero(s, "green"), matchOrReturnZero(s, "blue")

}

func part1() {
	games := readline.Readlines("input.txt")
	possibleGameIndices := 0
	for index, game := range games {
		sets := strings.Split(game, ";")
		maxRed := 0
		maxGreen := 0
		maxBlue := 0
		for _, s := range sets {
			red, green, blue := countMarbles(s)
			if red > maxRed {
				maxRed = red
			}
			if green > maxGreen {
				maxGreen = green
			}
			if blue > maxBlue {
				maxBlue = blue
			}
		}
		if maxRed <= 12 && maxGreen <= 13 && maxBlue <= 14 {
			possibleGameIndices += index + 1
		}
	}
	fmt.Println(possibleGameIndices)
}

func part2() {
	games := readline.Readlines("input.txt")
	totalPower := 0
	for _, game := range games {
		sets := strings.Split(game, ";")
		maxRed := 0
		maxGreen := 0
		maxBlue := 0
		for _, s := range sets {
			red, green, blue := countMarbles(s)
			if red > maxRed {
				maxRed = red
			}
			if green > maxGreen {
				maxGreen = green
			}
			if blue > maxBlue {
				maxBlue = blue
			}
		}
		totalPower += (maxRed * maxGreen * maxBlue)

	}
	fmt.Println(totalPower)
}

func main() {
	//part1()
	part2()
}
