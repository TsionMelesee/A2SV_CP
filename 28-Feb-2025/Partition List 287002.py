# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        left,right = dummy,dummy
        while right.next:
            if right.next.val < x:  
                temp = right.next  
                right.next = temp.next  
                temp.next = left.next
                left.next = temp
                if left == right: 
                    right = right.next 
                left = left.next  
            else:
                right = right.next  

        return dummy.next




        
        