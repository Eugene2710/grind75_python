from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        using fast and slow node, once fast reaches the end, return the slow node
        time complexity: O(N/2)
        space complexity: O(1)
        """
        slow: ListNode | None = head
        fast: ListNode | None = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow