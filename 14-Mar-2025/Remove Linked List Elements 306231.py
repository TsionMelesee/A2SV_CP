# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # print(head)
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        print(curr)
        while curr.next:
            if curr.next.val==val:
                
                temp = curr.next
                curr.next = curr.next.next
                temp.next=None
            else:
                curr=curr.next

        return dummy.next 
       