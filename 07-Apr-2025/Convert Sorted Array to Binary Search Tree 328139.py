# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        size = len(nums)
        mid = size // 2
        root = TreeNode(nums[mid])

        def dfs(nums, left, right, root):
            if left > right:
                return
            mid = (left + right) // 2
            if nums[mid] < root.val and not root.left:
                root.left = TreeNode(nums[mid])
                dfs(nums, left, mid - 1, root.left)
                dfs(nums, mid + 1, right, root.left)

            elif nums[mid] > root.val and not root.right:
                root.right = TreeNode(nums[mid])
                dfs(nums, left, mid - 1, root.right)
                dfs(nums, mid + 1, right, root.right)

            if root.left is None and root.right is None:
                root.left = TreeNode(nums[left]) if left <= right else None
                root.right = TreeNode(nums[right]) if left <= right else None

        dfs(nums, 0, mid - 1, root)
        dfs(nums, mid + 1, size - 1, root)
        return root
