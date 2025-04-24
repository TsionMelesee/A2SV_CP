# Problem: Maximum Sum of Two Non-Overlapping Subarrays - https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(firstLen, secondLen):
            val = sum(nums[:firstLen])
            ans = val
            idx = (0, firstLen - 1)
            arr = [0] * len(nums)
            arr[firstLen - 1] = val

            for end in range(firstLen, len(nums)):
                val += nums[end]
                val -= nums[end - firstLen]
                if val > ans:
                    ans = val
                    idx = (end - firstLen + 1, end)
                arr[end] = max(arr[end - 1], val)

            val2 = sum(nums[firstLen:firstLen + secondLen])
            ans2 = val2 + arr[firstLen - 1]

            for end2 in range(firstLen + secondLen, len(nums)):
                val2 += nums[end2]
                val2 -= nums[end2 - secondLen]
                ans2 = max(ans2, val2 + arr[end2 - secondLen])

            return ans2

        return max(
            maxSum(firstLen, secondLen),
            maxSum(secondLen, firstLen)
        )
