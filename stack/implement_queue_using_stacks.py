class MyQueue:
    """
    push: use append operations
    pop: append popped s1 value to s2 if s2 is empty and while s1 has values or else return popped value of s2
    peek: (similar to pop) append popped s1 value to s2 if s2 is empty and while s1 has values or else return s2[-1]
    """
    def __init__(self):
        self.s1: list(int) = []
        self.s2: list([int]) = []

    def push(self, x: int) -> None:
         self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2))==0