class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []
        for character in tokens:
            if character not in {'+', '-', '*', '/'}:
                tokenStack.append(int(character))
            else:
                num2 = int(tokenStack.pop())
                num1 = int(tokenStack.pop())
                if character == "+":
                    tokenStack.append(num1+num2)
                elif character == "-":
                    tokenStack.append(num1-num2)
                elif character == "*":
                    tokenStack.append(num1*num2)
                elif character == "/":
                    tokenStack.append(int(num1/num2))
        return tokenStack.pop()