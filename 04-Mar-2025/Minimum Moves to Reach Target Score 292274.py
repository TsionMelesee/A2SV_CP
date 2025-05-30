# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target>0 and maxDoubles>0:
            if target%2==0:
                ans+=1
                target = target/2
                maxDoubles-=1
            else:
                ans+=1
                target-=1
        ans+=(int(target-1))
        return ans

            

            

            
        