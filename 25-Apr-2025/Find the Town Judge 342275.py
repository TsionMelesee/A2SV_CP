# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = Counter()
        cnt2 = Counter()
        for i in trust:
            cnt[i[1]]+=1
            cnt2[i[0]]+=1
        for i in range(1,n+1):
            if cnt[i]==n-1 and cnt2[i]==0:
                return i
        return -1


        