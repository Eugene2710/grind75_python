from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1050 start
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2 pointers: l and r
        Cases:
        1. both lists are empty -> return empty list
        2. one list is empty -> return the other list
        3. both lists are not empty
        a. if l <= r

        b. if l > r

        c. .left=None or .right=None -> append the rest of the linked list to the res
        note: use the dummy for head and tail for end of res linked list to avoid start or end of linked lists errors

        time complexity: O(L+R)
        space complexity: O(1)
        """
        dummy: Optional[ListNode] = ListNode()
        head: Optional[ListNode] = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        return dummy.next