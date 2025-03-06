# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i] :
                val = stack.pop()
                dic[val]=nums2[i]
            stack.append(nums2[i])
        ans = []
        for i in nums1:
            if i in dic:
                ans.append(dic[i])
            else:
                ans.append(-1)
        return ans

        
        