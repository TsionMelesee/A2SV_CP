# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        l, r = len(nums) - 1, len(nums) - 1
        while l >= 0 and r > 0:
            if r == l or nums[l] == 0:
                l -= 1
            elif nums[l] >= r - l:
                r = l
                l -= 1
            else:
                l -= 1
        return r == 0
