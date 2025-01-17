from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ')':
                    if stack.pop() == '(':
                        continue
                    else:
                        return False
                elif c == '}':
                    if stack.pop() == '{':
                        continue
                    else:
                        return False
                elif c == ']':
                    if stack.pop() == '[':
                        continue
                    else:
                        return False
        return (len(stack)==0)