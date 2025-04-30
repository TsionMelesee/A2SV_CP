# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            if heights[i] < heights[i + 1]:
                heapq.heappush(heap, heights[i + 1] - heights[i])

            while  len(heap)>ladders  :
                if bricks >= heap[0]:
                    bricks -= heapq.heappop(heap)         
                elif ladders > 0:
                    heapq.heappop(heap)                   
                    ladders -= 1
                else:
                    return i
        return len(heights) - 1
