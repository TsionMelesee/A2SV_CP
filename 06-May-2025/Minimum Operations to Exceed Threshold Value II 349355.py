# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap =[]
        ans = 0
        for i in nums:
            heapq.heappush(heap,i)
        while len(heap)>1:
            if heap[0]>=k:
                break

            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            heapq.heappush(heap,min(x, y) * 2 + max(x, y))
            ans+=1
        return ans if heap[0] >= k else -1




        