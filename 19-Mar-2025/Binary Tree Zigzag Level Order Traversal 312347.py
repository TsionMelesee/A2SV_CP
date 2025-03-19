# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deq = deque()
        ans = []
        deq.append(root)
        idx= 0
        while len(deq)>0:
            arr = []
            for i in range(len(deq)):
                curr = deq.popleft()
                arr.append(curr.val)
                if curr.left:
                    deq.append(curr.left)
                if curr.right:
                    deq.append(curr.right)
            if idx%2==0:
                ans.append(arr)
            else:
                ans.append(arr[::-1]) 
            idx+=1
        return ans



            
        