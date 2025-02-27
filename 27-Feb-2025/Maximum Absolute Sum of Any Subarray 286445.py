# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_val = 0
        curr = 0
        min_val = 0
        curr2 = 0
        for i in nums:
            curr = max(curr,0)
            curr2 = min(curr2,0)
            curr2 +=i
            curr+=i
            max_val = max(max_val,curr)
            min_val = min(min_val,curr2)
        return max(abs(max_val),abs(min_val))
        