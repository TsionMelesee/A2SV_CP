# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.k = k
        self.value = value
        self.cnt = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        
        if num == self.value:
            self.cnt += 1
        
        if len(self.queue) > self.k:
            x = self.queue.popleft()
            if x == self.value:
                self.cnt -= 1
        
        return self.cnt == self.k

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)