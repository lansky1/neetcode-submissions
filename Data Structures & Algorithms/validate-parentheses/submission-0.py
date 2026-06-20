class Solution:
    def isValid(self, s: str) -> bool:
        stack_ = []
        for char in s:
            if char == ')' and len(stack_) > 0 and stack_[-1] == '(':
                stack_.pop()
            elif char == ']' and len(stack_) > 0 and stack_[-1] == '[':
                stack_.pop()
            elif char == '}' and len(stack_) > 0 and stack_[-1] == '{':
                stack_.pop()
            else:
                stack_.append(char)
        
        if len(stack_) > 0:
            return False
        return True
