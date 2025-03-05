# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(0)
        dummy.next = head
        arr = []
        curr = dummy.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # print(arr)
        max_val = -float('inf')
        n = len(arr)
        for i in range(len(arr)):
            max_val = max(max_val, arr[i] + arr[n - i - 1])
        
        return max_val
