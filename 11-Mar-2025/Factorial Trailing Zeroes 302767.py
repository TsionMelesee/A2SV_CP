# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n==1 or n ==0:
                return 1
            return n*factorial(n-1)
        x = factorial(n)
        ans = 0
        while x>0:
            if x%10!=0:
                break
            else:
                x//=10
                ans+=1
        return ans

        

        


        