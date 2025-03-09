# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r,l = 0,0
        cnt = 0
        for i in range(len(s)):
            if l == r:
                cnt+=1
                l=0
                r=0
            if s[i]=='R':
                r+=1
            if s[i]=='L':
                l+=1
        return cnt
        