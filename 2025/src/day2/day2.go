package main

import (
	"fmt"
	"input"
	"readline"
	"regexp"
	"strconv"
	"strings"
)

func isRepeating(s string) bool {
	accum := ""
	for len(accum)+1 < len(s) {
		accum = string(s[len(s)-1]) + accum
		s = s[:len(s)-1]
		if len(s)%len(accum) == 0 {
			isRepeating := true
			for i := 0; i < len(s); i += len(accum) {
				if s[i:i+len(accum)] != accum {
					isRepeating = false
				}
			}
			if isRepeating {
				return true
			}
		}
	}
	return false
}

func isTwice(s string) bool {
	accum := ""
	for len(accum)+1 < len(s) {
		accum = string(s[len(s)-1]) + accum
		s = s[:len(s)-1]
		if s == accum {
			return true
		}
	}
	return false
}

func main() {
	input.GetInputForYearAndDay(2025, 2)
	line := strings.Join(readline.Readlines("input.txt"), "")
	re := regexp.MustCompile(`(\d+)-(\d+)`)
	matches := re.FindAllStringSubmatch(line, -1)
	//fmt.Printf("%v\n", matches)
	twiceTotal := 0
	repeatingTotal := 0
	for _, m := range matches {
		lval, _ := strconv.Atoi(m[1])
		rval, _ := strconv.Atoi(m[2])
		for i := lval; i <= rval; i++ {
			s := strconv.Itoa(i)
			if isTwice(s) {
				twiceTotal += i
			}
			if isRepeating(s) {
				repeatingTotal += i
			}
		}
	}
	fmt.Printf("part1: %d\npart2: %d\n", twiceTotal, repeatingTotal)
}
