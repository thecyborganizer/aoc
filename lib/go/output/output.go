package output

import "fmt"

func PrintGrid(grid [][]string) {
	for _, row := range grid {
		for _, r := range row {
			fmt.Printf("%s", r)
		}
		fmt.Printf("\n")
	}
}
