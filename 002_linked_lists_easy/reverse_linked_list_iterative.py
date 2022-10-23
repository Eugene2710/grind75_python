Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative method
        Approach: change the direction of pointer by using 2 pointers and temp variable - from curr = prev.next to prev = curr.next
        Note: remb to initialize prev to None so that the last node.next after reversal is true, and that the while loop can run
        Time Complexity = O(N)
        Space Compexity = O(1)
        """
        curr: Optional[Listnode] = head
        prev: Optional[ListNode] = None

        while curr:
            nxt: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev