package main

import "fmt"

func convert(s string, numRows int) string {
	if numRows <= 1 || numRows >= len(s) {
		return s
	}
	rows := make([]string, numRows)
	down := true
	counter := 0
	zigPos := 0
	for counter < len(s) {
		rows[zigPos] += string(s[counter])

		if down {
			if zigPos == numRows-1 {
				down = false
				zigPos = numRows - 2
			} else {
				zigPos = zigPos + 1
			}
		} else {
			if zigPos == 0 {
				down = true
				zigPos = 1
			} else {
				zigPos = zigPos - 1
			}
		}

		counter++
	}

	result := ""
	for i := 0; i < numRows; i++ {
		result += rows[i]
	}
	return result
}
func main() {
	fmt.Println(convert("PAYPALISHIRING", 4))
}
