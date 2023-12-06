package main

import (
	"fmt"
	"math"
	"readline"
	"strings"
)

// array of [dest, src, range]
type mapType [][]int

func mapLookup(val int, m mapType) int {
	for _, e := range m {
		dest := e[0]
		src := e[1]
		length := e[2]
		if val >= src && val < src+length {
			return dest + (val - src)
		}
	}
	return val
}

func part1() {
	lines := readline.Readlines("input.txt")
	seeds := readline.GetAllNumbers(lines[0])
	maps := []mapType{}
	mapsIndex := -1
	for i := 1; i < len(lines); i++ {
		if len(lines[i]) < 3 {
			continue
		} else if strings.HasSuffix(lines[i], ":") {
			mapsIndex++
			maps = append(maps, mapType{})
		} else {
			numbers := readline.GetAllNumbers(lines[i])
			maps[mapsIndex] = append(maps[mapsIndex], numbers)
		}
	}
	locations := []int{}
	for _, seed := range seeds {
		val := seed
		for _, m := range maps {
			val = mapLookup(val, m)
		}
		locations = append(locations, val)
	}
	minimum := math.MaxInt
	for _, l := range locations {
		if l < minimum {
			minimum = l
		}
	}
	fmt.Printf("%d\n", minimum)

}

func part2() {
	lines := readline.Readlines("input.txt")
	seeds := readline.GetAllNumbers(lines[0])
	maps := []mapType{}
	mapsIndex := -1
	for i := 1; i < len(lines); i++ {
		if len(lines[i]) < 3 {
			continue
		} else if strings.HasSuffix(lines[i], ":") {
			mapsIndex++
			maps = append(maps, mapType{})
		} else {
			numbers := readline.GetAllNumbers(lines[i])
			maps[mapsIndex] = append(maps[mapsIndex], numbers)
		}
	}
	minimum := math.MaxInt
	for i := 0; i < len(seeds); i += 2 {
		for seed := seeds[i]; seed < seeds[i]+seeds[i+1]; seed++ {
			val := seed
			for _, m := range maps {
				val = mapLookup(val, m)
			}
			if val < minimum {
				minimum = val
			}
		}
	}
	fmt.Printf("%d\n", minimum)

}

func main() {
	//part1()
	part2()
}
