# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q:'TreeNode') -> 'TreeNode':
        def recur(root):
            if not root:
                return
            
            if (p.val <= root.val <= q.val)  or (q.val<= root.val <= p.val):
                return root

            if p.val>= root.val:
                return recur(root.right)
            else:
                return recur(root.left)

        return recur(root)

    
