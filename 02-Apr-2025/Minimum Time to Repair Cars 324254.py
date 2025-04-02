# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(mid):
            total_cars = 0
            for r in ranks:
                total_cars += int((mid // r) ** 0.5)
            return total_cars >= cars
        
        left, right = 0, max(ranks)*(cars ** 2)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            