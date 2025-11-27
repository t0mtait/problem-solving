package main

import (
	"math/big"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	pos := big.NewInt(1)
	x := big.NewInt(0)
	y := big.NewInt(0)

	for l1 != nil {
		val := big.NewInt(int64(l1.Val))
		term := new(big.Int).Mul(val, pos)
		x.Add(x, term)
		pos.Mul(pos, big.NewInt(10))
		l1 = l1.Next
	}

	pos = big.NewInt(1)
	for l2 != nil {
		val := big.NewInt(int64(l2.Val))
		term := new(big.Int).Mul(val, pos)
		y.Add(y, term)
		pos.Mul(pos, big.NewInt(10))
		l2 = l2.Next
	}
	z := new(big.Int).Add(x, y)
	a := z.String() // "123456..." as string

	ans := &ListNode{Val: int(a[len(a)-1] - '0')}
	tail := ans
	for i := len(a) - 2; i >= 0; i-- {
		newNode := &ListNode{Val: int(a[i] - '0')}
		tail.Next = newNode
		tail = newNode
	}
	return ans
}
