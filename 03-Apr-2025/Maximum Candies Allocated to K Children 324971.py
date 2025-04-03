# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid(mid):
            ttl = 0
            for i in candies:
                ttl+=(i//mid)
            return ttl>=k
        left,right = 1,max(candies)
        ans = 0
        while left<=right:
            mid = (left+right)//2
            if valid(mid):
                ans = mid
                left = mid+1
            else:
                right=mid-1
        return ans
        