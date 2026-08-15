class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    r = stack[-2] + stack[-1]
                elif tokens[i] == '-':
                    r = stack[-2] - stack[-1]
                elif tokens[i] == '*':
                    r = stack[-2] * stack[-1]
                elif tokens[i] == '/':
                    r = int(stack[-2] / stack[-1])

                stack.pop()
                stack.pop()
                stack.append(r)
        return stack[-1]
        