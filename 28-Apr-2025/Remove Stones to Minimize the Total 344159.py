# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        while k>0:
            val = -heapq.heappop(piles)
            heapq.heappush(piles,-(val-(val//2)))
            k-=1
        return sum(piles)*-1
        
            
