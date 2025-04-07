# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def valid(k):
            diff = [0] * (len(nums) + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < len(nums):
                    diff[r + 1] -= v

            ans = 0
            for i in range(len(nums)):
                ans += diff[i]
                if ans < nums[i]:
                    return False
            return True

        l, r = 0, len(queries)
        ans = -1
        
        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
