class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
        return "".join(stack)