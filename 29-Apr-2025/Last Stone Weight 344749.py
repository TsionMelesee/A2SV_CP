# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x!=y:
                heapq.heappush(stones,-(y-x))
        
        return -stones[0] if len(stones)>0 else 0
        