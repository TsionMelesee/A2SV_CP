# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for i in counter:
            if i ==0:
                ans+=counter[i]
            else:
                if counter[i]<=i+1:
                    ans+=i+1
                else:
                    print((3//2))
                    ans+=(i+1)*((counter[i]+i)//(i+1))
                    

        return ans

            

        