# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        simplify_path = path.split('/')
        stack = []
        for i in simplify_path:
            if i == '..' and stack:
                stack.pop()
            if i != '' and i != '..' and i != '.':
                stack.append(i)
        ans ='/'.join(stack) 
        return '/'+ans
