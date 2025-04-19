from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Using 3 pointers, curr prev next, reassign them and move on to next node
        time complexity: O(N)
        space complexity: O(1)
        """
        curr: ListNode | None = head
        prev: ListNode | None = None
        while curr:
            next: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev