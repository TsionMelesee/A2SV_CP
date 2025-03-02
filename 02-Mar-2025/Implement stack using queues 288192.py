# Problem: Implement stack using queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.queue2 = deque()

        

    def push(self, x: int) -> None:
        self.queue.append(x)

        

    def pop(self) -> int:
        while len(self.queue)>1:
            self.queue2.append(self.queue.popleft())
        x = self.queue.popleft()
        while len(self.queue2)>0:
            self.queue.append(self.queue2.popleft())

        self.queue2.clear()

        return x


    def top(self) -> int:
        while len(self.queue) > 1:
            self.queue2.append(self.queue.popleft())
        x = self.queue[0]
        self.queue2.append(self.queue.popleft())
        while len(self.queue2) > 0:
            self.queue.append(self.queue2.popleft())
        self.queue2.clear()
        return x
        


        

    def empty(self) -> bool:
        return len(self.queue)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()