# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Tortoise and Hare Method - iterate through linked list using 1 slow and 1 fast pointer. Return false if slow pointer == fast pointer.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False