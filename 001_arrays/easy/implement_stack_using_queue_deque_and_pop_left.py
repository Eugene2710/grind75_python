class MyStack:
    """
    Approach: Using a double ended queue, pop requires the last int of the stack to be the zeroth index - push the ones at the start to the top of the stack, and remove the ones in front of the last item of stack. The rest are pretty much the same.
    Time Complexity: pop - O(N), the rest are O(1)
    Space Complexity: O(N)
    """

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0