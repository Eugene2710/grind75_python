# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Create a hashmap which contains each node that was cycled. If node exists in the hashmap return false. Terminate if node.next == null.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        traversed: Optional(Listnode) = set()

        while head:
            if head not in traversed:
                traversed.add(head.next)
                head = head.next
            else:
                return True

        return False
