# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        binary = sorted(s,reverse =True)
        binary.append("1")
        binary.pop(0)
        return ''.join(binary)
        
        

        

        