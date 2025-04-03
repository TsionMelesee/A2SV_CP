# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        # print(bucket)
        for i,v in cnt.items():
            bucket[v].append(i)
        ans = []
        # print(bucket)
        for i in range(len(bucket)-1,-1,-1):
            if len(ans)==k:
                break
            else:
                if bucket[i]:
                    ans.extend(bucket[i])
        return ans

        
