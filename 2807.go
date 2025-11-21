package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	ptr := head
	for head != nil && head.Next != nil {
		newNode := &ListNode{
			Val:  gcd(head.Val, head.Next.Val),
			Next: head.Next,
		}
		head.Next = newNode
		head = newNode.Next
	}
	return ptr
}
