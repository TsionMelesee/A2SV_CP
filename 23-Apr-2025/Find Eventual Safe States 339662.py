# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        order = []
        color = [0 for _ in range(len(graph))]
        def dfs(node):
            if color[node]==1:
                return False
            color[node]=1
            for i in graph[node]:
                if color[i]==2:
                    continue
                if not dfs(i):
                    return False
            color[node]=2
            order.append(node)
            return True

        
        for i  in range(len(graph)):
            if color[i]==0:
                dfs(i)
        order.sort()
        return order
                

            
