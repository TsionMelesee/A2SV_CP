# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0 
        high = x
        while(low <= high):
            mid = (high + low)//2
            if (mid **2) == x:
                return mid
            elif(mid **2) > x:
                high = mid -1
            elif(mid **2) < x:
                low = mid + 1
        return high

        