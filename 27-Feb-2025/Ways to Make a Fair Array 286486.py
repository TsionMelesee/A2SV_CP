# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_acc = 0
        even_acc = 0
        ans = 0
        even,odd = 0,0
        for i in range(len(nums)):
            if i%2==0:
                even_acc+=nums[i]
            else:
                odd_acc+=nums[i]
        for i in range(len(nums)):
            if i %2==0:
                if even_acc-even+odd-nums[i]==odd_acc-odd+even:
                    ans+=1
                even+=nums[i]
            else:
                if odd_acc-odd+even-nums[i]==even_acc-even+odd:
                    ans+=1
                odd+=nums[i]
        return ans

