# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ans = set()
        curr = root
        queue = deque()
        queue.append(root)
        # print(queue)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # print(node)
                ans.add(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        # print(ans)
        return len(ans)==1
        
            

        