# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)-2,0,-1):
            c = nums[i+1]
            if nums[i]+nums[i-1]>c:
                return nums[i]+nums[i-1]+c
        return 0




        

        