# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows - 1
        ans = 0
        while l <= r:
            row = (l + r) // 2
            if target > matrix[row][-1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row - 1
            else:
                ans = row
                break
        else:
            return False
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[ans][mid]:
                l = mid + 1
            elif target < matrix[ans][mid]:
                r = mid - 1
            else:
                return True

        return False
