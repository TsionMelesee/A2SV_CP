# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def ancestordiff(root, min_val, max_val):
            if not root:
                return max_val-min_val
            max_val = max(max_val,root.val)
            min_val = min(min_val,root.val)
            return max(ancestordiff(root.left,min_val,max_val),ancestordiff(root.right,min_val,max_val))
        return ancestordiff(root, float('inf'), float('-inf'))

        
       