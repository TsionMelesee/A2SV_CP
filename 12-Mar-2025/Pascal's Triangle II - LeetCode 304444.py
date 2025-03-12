# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = 0
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        if rowIndex ==2:
            return [1,2,1]
        
        arr = self.getRow(rowIndex-1)
        result = []
        for i in range(0, len(arr)-1):
            result.append(arr[i] + arr[i+1])
    
        return [1]+result+[1]

        