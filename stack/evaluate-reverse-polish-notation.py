class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        stack = []
        for t in tokens:
            if is_number(t):
                stack.append(int(t))
            else:
                if t == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                if t == "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                if t == "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a*b)
                if t == "/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
        return stack[0]