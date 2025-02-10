from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(openP, closeP):
            if openP == closeP == n:
                ans.append("".join(stack))
                return

            if closeP < openP:
                stack.append(')')
                backtrack(openP, closeP + 1)
                stack.pop()

            if openP < n:
                stack.append('(')
                backtrack(openP + 1, closeP)
                stack.pop()
        backtrack(0,0)
        return ans
