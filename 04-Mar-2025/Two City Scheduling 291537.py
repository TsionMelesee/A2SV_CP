# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        for i in range(len(costs)):
            arr.append((costs[i][-1]-costs[i][0],i))
        arr.sort()
        ans = 0
        for i in range(len(costs)):
            if i<len(costs)//2:
                ans+=costs[arr[i][-1]][-1]
            else:
                ans+=costs[arr[i][-1]][0]
        return ans
        