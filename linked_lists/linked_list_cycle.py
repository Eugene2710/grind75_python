from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        2 pointers: one fast, one slow
        keep iterating until slow pointer reaches the end
        Cases:
        1. there is a cycle -> fast=slow
        2. there is no cycle -> fast.next = None
        note: remember to check for fast.next as well or else fast.next.next will return an error

        time complexity: O(N)
        space complexity: O(1)
        """
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False