class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []
        operators = {"+", "-", "*", "/"}
        for character in tokens:
            if character not in operators:        # handles negatives & multi-digit numbers
                tokenStack.append(int(character))
            else:
                num2 = int(tokenStack.pop())
                num1 = int(tokenStack.pop())
                if character == "+":
                    tokenStack.append(num1+num2)
                if character == "-":
                    tokenStack.append(num1-num2)
                if character == "*":
                    tokenStack.append(num1*num2)
                if character == "/":
                    tokenStack.append(int(num1/num2))
        return tokenStack.pop()
