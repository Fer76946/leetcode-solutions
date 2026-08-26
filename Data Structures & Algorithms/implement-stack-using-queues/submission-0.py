class MyStack:

    def __init__(self):
        self.stacky = collections.deque()

    def push(self, x: int) -> None:
        self.stacky.append(x)

    def pop(self) -> int:
        for i in range(len(self.stacky) - 1):
            self.push(self.stacky.popleft())
        return self.stacky.popleft()

    def top(self) -> int:
        return self.stacky[-1]

    def empty(self) -> bool:
        return len(self.stacky) == 0
            


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()