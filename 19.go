package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	totalNodes := 1
	cur := head
	for cur.Next != nil {
		totalNodes += 1
		cur = cur.Next
	}
	if totalNodes == 1 {
		return nil
	}
	if totalNodes == n {
		return head.Next
	}
	cur = head
	it := 0
	// navigate to the node before the one to be removed
	for it < totalNodes-n-1 {
		cur = cur.Next
		it++
	}
	//repoint node
	if cur.Next != nil && cur.Next.Next != nil {
		cur.Next = cur.Next.Next
		fmt.Println("pointing", cur.Val, "towards", cur.Next.Val)

	} else {
		cur.Next = nil
	}
	return head
}
