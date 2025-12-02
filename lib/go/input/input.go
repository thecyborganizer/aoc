package input

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

func GetInputForYearAndDay(year int, day int) {
	if _, err := os.Stat("input.txt"); err == nil {
		return
	}
	file, err := os.Open("../../../cookie.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	bytes, err := io.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}
	client := &http.Client{}
	path := fmt.Sprintf("https://adventofcode.com/%d/day/%d/input", year, day)
	req, err := http.NewRequest("GET", path, nil)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("Cookie", string(bytes))
	res, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	body, err := io.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	outfile, err := os.Create("input.txt")
	if err != nil {
		fmt.Printf("Unable to open input.txt for caching\n")
	} else {
		_, err := io.Writer.Write(outfile, body)
		if err != nil {
			log.Fatal(err)
		}
	}
}
