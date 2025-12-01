package main

import (
	"fmt"
	"input"
	"readline"
	"regexp"
	"strconv"
)

func main() {
	input.GetInputForYearAndDay(2025, 1)
	lines := readline.Readlines("input.txt")
	//lines := readline.Readlines("test.txt")

	re := regexp.MustCompile(`([LR])(\d+)`)
	rot := 50
	pointCount := 0
	clickCount := 0
	for _, l := range lines {
		sm := re.FindStringSubmatch(l)
		dir := sm[1]
		val, _ := strconv.Atoi(sm[2])
		for i := 0; i < val; i++ {
			if dir == "L" {
				rot -= 1
			} else {
				rot += 1
			}
			if i != val-1 && rot%100 == 0 {
				clickCount += 1
			}
		}
		rot = (rot%100 + 100) % 100
		if rot == 0 {
			pointCount += 1
		}
	}
	fmt.Printf("pt1: %d\n", pointCount)
	fmt.Printf("pt2: %d\n", clickCount+pointCount)
}
