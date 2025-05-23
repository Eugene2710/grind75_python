class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        list of zero elem of length temp to store final results
        nested stack to consider temp which are less warm
        iterate through temp, enum it, while current elem > top elem in stack:
        pop elem in stack and append diff to res
        append the index and elem to stack

        time complexity: O(N)
        space complexity: O(N)
        """
        res: list[int] = [0] * len(temperatures)
        stack: list[list[int]] = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i-stackI)
            stack.append([t, i])

        return res