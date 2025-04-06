# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        ans = []
        for i in arr:
            x = abs(i) - 1
            if  arr[x]> 0:
                arr[x] = -arr[x]
            else:
                ans.append(abs(i))
        for i in range(len(arr)):
            if arr[i] > 0:
                ans.append(i + 1) 
        
        return ans
