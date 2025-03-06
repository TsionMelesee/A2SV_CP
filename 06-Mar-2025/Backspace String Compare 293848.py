# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i =='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        for i in t:
            if i =='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        return stack1 == stack2

        