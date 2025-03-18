# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        def symmerty(left,right):
            if left and right:
                if left and right and left.val!=right.val:
                    return False
                return symmerty(left.left,right.right) and symmerty(left.right,right.left)
            elif not left and right:
                return False
            elif not right and left:
                return False
            else:
                return True
        return symmerty(left,right)

        