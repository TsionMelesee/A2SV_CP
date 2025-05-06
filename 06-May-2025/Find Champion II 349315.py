# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_deg = [0] * n
        nodes = set()
        arr = []
        for a, b in edges:
            graph[a].append(b)
            in_deg[b] += 1
            nodes.add(a)
            nodes.add(b)
            
        for i in range(n):
            if in_deg[i]==0:
                arr.append(i)

        if len(arr) == 1:
            return arr[0]
        return -1
        