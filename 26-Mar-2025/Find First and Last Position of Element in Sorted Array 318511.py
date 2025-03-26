# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        ans = []

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                ans.append(mid)
                start = mid
                break
            elif nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1

        if not ans:
            return [-1, -1]

        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target):
                ans.append(mid)
                break
            elif nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

        if len(ans) == 1:
            ans.append(-1)

        return ans
