class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Use stack to append popped values for + and * operations.
        Assign tmp values to popped values from stack before - and / before appendding final value - order matters.

        time complexity: O(N)
        space complexity: O(N)
        """
        stack: list[int] = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(b-a) # order matters
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))

        return stack[0]
