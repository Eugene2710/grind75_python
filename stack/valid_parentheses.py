class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use a stack and dictionary. Check against dict if item matches
        If matches, pop. Else, return false.

        time complexity: O(N)
        space complexity: O(N)
        """
        stack: list[str] = []
        check: dict[str, str] = {")": "(", "]": "[", "}": "{"}

        for a in s:
            # if it is a closed bracket
            if a in check:
                # check if stack is not empty and top of parenthesis is a pair w current value in array
                if stack and stack[-1] == check[a]:
                    stack.pop()
                else:
                    return False

            # if it is an open bracket
            else:
                stack.append(a)

        return True if not stack else False