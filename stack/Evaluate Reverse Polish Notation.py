from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                last = stack.pop() 
                src = stack.pop()
                stack.append(src - last)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                last = stack.pop() 
                src = stack.pop()
                stack.append(int(src / last))
            else:
                stack.append(int(token))
        return stack.pop()