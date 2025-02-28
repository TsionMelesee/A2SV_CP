# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left,right =l1,l2
        dummy = ListNode()
        curr = dummy
        rem = 0
        while left or right:
            val = 0
            if left:
                val+=left.val
            if right:
                val+=right.val
            if val+rem>9 :
                curr.next= ListNode(int(str(val+rem)[-1]))
                rem = 1
            else:
                curr.next =ListNode(val+rem)
                rem = 0
            if left:
                left = left.next
            if right:
                right = right.next
            
            curr = curr.next
        if rem>0:
            curr.next = ListNode(1)

        return dummy.next
            
            