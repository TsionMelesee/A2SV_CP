# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        cnt = Counter(nums)
        for i in cnt:
            if cnt[i]==2:
                answer.append(i)
        return answer


            

        