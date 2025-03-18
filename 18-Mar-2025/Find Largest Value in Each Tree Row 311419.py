# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=defaultdict(list)
        l,r = 0,0
        def largest(root,l,arr):
            if root:
                arr[l].append(root.val)
                largest(root.left,l+1,arr)
                largest(root.right,l+1,arr)
            return
        largest(root,l,ans)
        arr = []
        for i in ans:
            arr.append(max(ans[i]))
        return arr



                


                




        