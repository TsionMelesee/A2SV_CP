# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        answer = 0
        ans = [0] * len(arr) 
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                prev = stack[-1]
                ans[i] = ans[prev] + (i - prev) * arr[i]  
            else:
                prev = -1
                ans[i] = (i - prev) * arr[i] 

            
            answer += ans[i]
            answer %= (10**9 + 7)

            stack.append(i)

        return answer
