# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i=='C':
                stack.pop()
            elif i =='D':
                val = stack[-1]
                stack.append(2*val)
            elif i =='+':
                val1= stack[-1]
                val2 = stack[-2]
                stack.append(val1+val2)
            else:
                stack.append(int(i))
        return sum(stack)


        