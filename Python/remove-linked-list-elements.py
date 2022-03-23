"""
LeetCode[https://leetcode-cn.com/problems/remove-linked-list-elements/]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode<{self.val}>"


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = ListNode(val=nodes.pop(0))
            print(node)
            self.head = node
            for elem in nodes:
                node.next = ListNode(val=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        return f"{nodes}"


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next


if __name__ == "__main__":
    linked_list = LinkedList(nodes=[1, 2, 6, 3, 4, 5, 6])
    print(linked_list)
    val = 6
    solution = Solution()
    solution.removeElements(linked_list.head, val)
    print(linked_list)
