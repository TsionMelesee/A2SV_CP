# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def kth(n):
            if n ==1:
                return '0'
            temp = kth(n-1)
            x = ''
            for i in temp:
                if i =='0':
                    x+='1'
                else:
                    x+='0'
            
            return temp +'1'+x[::-1]
        return kth(n)[k-1]
        
            
            