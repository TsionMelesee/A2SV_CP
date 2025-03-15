# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        x = 0  
        player = n  

        while player > 1:
            cnt = 0  
            while cnt < k:  
                if arr[x] > 0:  
                    cnt += 1
                if cnt == k:
                    break
                x = (x + 1) % n  
            arr[x] = -1  
            player -= 1  

            while arr[x] < 0:  
                x = (x + 1) % n  

        return max(arr)  
