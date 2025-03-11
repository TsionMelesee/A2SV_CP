# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False

        def powoffour(n):
            if n ==1:
                return True
            elif n%4!=0:
                return False
            return powoffour(n//4)
        return powoffour(n)
        