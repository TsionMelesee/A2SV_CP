# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        left = root.left
        right = root.right
        def reverse(left,right,l):
            if left:
                if l %2 !=0:
                    left.val,right.val = right.val,left.val
                l+=1
                reverse(left.left,right.right,l)
                reverse(left.right,right.left,l)
            return
        reverse(left,right,1)
        return root
        