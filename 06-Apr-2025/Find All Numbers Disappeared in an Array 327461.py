# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        ans = []
        for i in arr:
            x = abs(i) - 1
            if  arr[x]> 0:
                arr[x] = -arr[x]
        for i in range(len(arr)):
            if arr[i] > 0:
                ans.append(i + 1) 
        
        return ans
