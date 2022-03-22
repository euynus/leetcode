/*
 * @lc app=leetcode id=203 lang=golang
 *
 * [203] Remove Linked List Elements
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    dummy := new(ListNode)
    dummy.Next = head
    for p := dummy; p.Next != nil; {
        if (p.Next.Val == val) {
            p.Next = p.Next.Next
        } else {
            p = p.Next
        }
    }
    return dummy.Next
}
// @lc code=end

