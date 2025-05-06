# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = defaultdict(lambda: [0, []])
        ans = 0
        for i in employees:
            dic[i.id][0]+=i.importance
            dic[i.id][1].extend(i.subordinates)

        def dfs(emp):
            total = dic[emp][0]
            for i in dic[emp][1]:
                total += dfs(i)
            return total

        return dfs(id)

        
        