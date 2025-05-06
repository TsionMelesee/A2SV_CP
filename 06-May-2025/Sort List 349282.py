# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(head):
            if not head:
                return head
            slow = fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def merge(left,right):
            dummy = ListNode()
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                    curr = curr.next
                else:
                    curr.next = right
                    right = right.next
                    curr = curr.next
            while left:
                curr.next = left
                left = left.next
                curr = curr.next
            while right:
                curr.next = right
                right = right.next
                curr = curr.next
            return dummy.next
        def merge_sort(head):
            if not head or not head.next:
                return head
            half = middle(head)
            left = head
            right = half.next
            half.next = None
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left,right)
        return merge_sort(head)


                

 
        