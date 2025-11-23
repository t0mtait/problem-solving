package main

import (
	"strconv"
	"strings"
)

func myAtoi(s string) int {
	s = strings.TrimLeft(s, " ")
	positive := (strings.Index(s, "-") != 0)
	if positive {
		s = strings.TrimPrefix(s, "+")
	} else {
		s = strings.TrimPrefix(s, "-")
	}
	s = strings.TrimLeft(s, "0")
	// get the index of any non-digit character
	x := strings.IndexFunc(s, func(r rune) bool {
		return r < '0' || r > '9'
	})
	if x != -1 {
		s = s[:x]
	}
	num, err := strconv.Atoi(s)
	if err != nil {
		if (err.Error() == "strconv.Atoi: parsing \"\": invalid syntax") || len(s) == 0 {
			return 0
		}
		if positive {
			return 2147483647
		} else {
			return -2147483648
		}
	}

	if positive {
		if num > 2147483647 {
			num = 2147483647
		}
		return num
	} else {
		if num > 2147483647 {
			num = 2147483648
		}
		return num - (2 * num)
	}
}
