# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = []
        def sumRoot(root, x):
            if not root:
                return
            x += str(root.val)
            if not root.left and not root.right:
                ans.append(int(x))
                return


            sumRoot(root.left, x) 
            sumRoot(root.right,x)

        sumRoot(root, '')
        return sum(ans)
        
        

       

