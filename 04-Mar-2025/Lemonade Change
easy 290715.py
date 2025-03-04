# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0
        for i in bills:
            if i == 5:
                five+=5
            elif i == 10:
                if five>=5:
                    five-=5
                    ten+=10
                else:
                    return False
            elif i == 20:
                if five>=5 and ten>=10:
                    five-=5
                    ten-=10

                elif five>=15:
                    five-=15
                
                
                else:
                    return False
        return True
            
                