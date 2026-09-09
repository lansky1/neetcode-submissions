class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingBracketDict = {"}": "{", "]": "[", ")": "("}

        for c in s:
            if c in closingBracketDict:
                if stack and stack[-1] == closingBracketDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) 

        return True if len(stack) == 0 else False