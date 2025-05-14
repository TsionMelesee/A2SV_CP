# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        arr =[]
        while l<len(word1) and r<len(word2):
            arr.append(word1[l])
            arr.append(word2[r])
            l+=1
            r+=1
        arr.extend(word1[l:])
        arr.extend(word2[r:])
        return ''.join(arr)

        