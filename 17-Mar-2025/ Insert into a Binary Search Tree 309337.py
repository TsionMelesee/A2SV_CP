# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insert(root,val):
            if root.val>val:
                if root.left:
                    return insert(root.left,val)
                else:
                    root.left = TreeNode(val)
                    return 
            if root.val<val:
                if root.right:
                    return insert(root.right,val)
                else:
                    root.right  =TreeNode(val)
                    return 
        insert(root,val)
        return root

        