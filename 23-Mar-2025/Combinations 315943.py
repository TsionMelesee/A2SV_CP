# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(num,path):
            if len(path)==k:
                ans.append(path[:])
                return
            if num>n:
                return
            path.append(num)
            backtracking(num+1,path)
            path.pop()

            backtracking(num+1,path)
            
        backtracking(1,[])
        return ans
            


        