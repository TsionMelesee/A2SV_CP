# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(mid):
            total = 0
            for i in piles:
                total+=ceil(i/mid)
            return total<=h

        left,right,ans = 1,max(piles),0
        while left<=right:
            mid = (left+right)//2
            if good(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans


        