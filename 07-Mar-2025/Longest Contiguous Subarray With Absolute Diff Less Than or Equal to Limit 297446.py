# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        ans = float("-inf")
        left = 0

        for i in range(len(nums)):
            while inc and inc[-1] > nums[i]:
                inc.pop()
            inc.append(nums[i])

            while dec and dec[-1] < nums[i]:
                dec.pop()
            dec.append(nums[i])

            while dec[0] - inc[0] > limit:
                if dec[0] == nums[left]:
                    dec.popleft()
                if inc[0] == nums[left]:
                    inc.popleft()
                left += 1
            ans = max(i - left + 1, ans)

        return ans