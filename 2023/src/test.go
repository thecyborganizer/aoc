package main

import (
	"fmt"
	"readline"
)

func main() {
	lines := readline.Readlines("../inputs/test.txt")
	fmt.Println(lines)
}
