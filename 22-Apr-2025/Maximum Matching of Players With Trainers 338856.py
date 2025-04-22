# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        play,train = len(players)-1,len(trainers)-1
        ans = 0
        while play>=0 and train>=0:
            if trainers[train] <players[play]:
                play-=1
            else:
                ans+=1
                play-=1
                train-=1
        return ans

        