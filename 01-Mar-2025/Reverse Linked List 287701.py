# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        after = dummy.next
        prev = None
        while dummy.next:
            after = after.next
            dummy.next.next = prev
            prev = dummy.next
            dummy.next = after
        return prev
     