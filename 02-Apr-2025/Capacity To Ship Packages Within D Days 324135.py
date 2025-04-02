# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(mid):
            ttl = 0
            cnt =0
            for i in weights:
                if ttl+i>mid:
                    cnt+=1
                    ttl = i
                else:
                    ttl+=i
            return cnt+1 <=days
        left,right = max(weights),sum(weights)
        ans = 0
        while left<=right:
            mid  =(left+right)//2
            if valid(mid):
                ans = mid
                right = mid-1
                
            else:
                left=mid+1
        return ans
                
            
    
