# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        arr = [0] * numCourses
        queue = deque()
        ans = []
        for course, pre in prerequisites:
            graph[pre].append(course)
            arr[course] += 1
        for course in range(numCourses):
            if arr[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            ans.append(course)

            for neighbor in graph[course]:
                arr[neighbor] -= 1
                if arr[neighbor] == 0:
                    queue.append(neighbor)

        if len(ans) != numCourses:
            return []

        return ans
