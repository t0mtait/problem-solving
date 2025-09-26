
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    let head: ListNode | null = null
    let tail: ListNode | null = null
    
    function addNode(node: ListNode) {
        if (head == null) {
            head = node
            tail = head
        } else {
            tail!.next = node
            tail = node
        }
    }
    
    while (list1 != null || list2 != null) {
        if (list1 == null) {
            addNode(list2!)
            list2 = list2!.next
        } else if (list2 == null) {
            addNode(list1)
            list1 = list1.next
        } else if (list1.val <= list2.val) {
            addNode(list1)
            list1 = list1.next
        } else {
            addNode(list2)
            list2 = list2.next
        }
    }
    
    return head
};

