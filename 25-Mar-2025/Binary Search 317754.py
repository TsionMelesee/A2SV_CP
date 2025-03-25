# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums)-1
        start =0
        def binary(start,end):
            mid = (end+start)//2
            if start>end:
                return -1
            elif nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return binary(mid+1,end)
            else:
                return binary(start,mid-1)
        return binary(start,end)


        