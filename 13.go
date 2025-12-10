package main

import "fmt"

func romanToInt(s string) int {
	ans := 0
	ch := 0
	i := 0
	ls := 100
	sym := [7]rune{'I', 'V', 'X', 'L', 'C', 'D', 'M'}
	val := [7]int{1, 5, 10, 50, 100, 500, 1000}
	for ch < len(s) {
		i = 0
		for i < 7 {
			if rune(s[ch]) == sym[i] {
				if ls < i {
					ans += val[i] - 2*val[ls]
				} else {
					ans += val[i]
				}
				fmt.Println(ans)
				ls = i
			}
			i++
		}
		ch++
	}
	return ans
}

func main() {
	s := "MCMXCIV"
	fmt.Println(romanToInt(s))
}
