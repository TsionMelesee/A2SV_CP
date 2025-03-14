# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = []
        temp = []
        for i in s:
            if i.isdigit():
                if stack and isinstance(stack[-1], int):
                    stack.append(int(str(stack.pop()) + i))
                else:
                    stack.append(int(i))
            elif i != ']':
                stack.append(i)
            elif i == ']':
                while stack and stack[-1] != '[': 
                    x = stack.pop()
                    temp.append(x)
                stack.pop()
                cnt = stack.count('[')

                temp = temp[::-1] * stack.pop()  
                if cnt == 0:
                    while stack:
                        temp.insert(0, stack.pop())
                    ans.append(''.join(temp))
                else:
                    stack.extend(temp)
                temp.clear()
        if stack:
            while stack:
                temp.insert(0, stack.pop())  
            ans.append(''.join(temp))
        return ''.join(ans)
