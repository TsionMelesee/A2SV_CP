# Problem: Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(list)
        ans = 0
        for i in range(len(nums)):
            if nums[i] in cnt:
                for j in cnt[nums[i]]:
                    if (j*i)%k==0:
                        ans+=1
            cnt[nums[i]].append(i)
        return ans


            

