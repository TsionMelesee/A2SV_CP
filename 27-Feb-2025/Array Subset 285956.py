# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a_cnt = Counter(a)
        b_cnt = Counter(b)
        for i in b_cnt:
            if b_cnt[i] > a_cnt[i]:
                    return False
        return True
    
    