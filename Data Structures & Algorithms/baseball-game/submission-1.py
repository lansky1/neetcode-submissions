class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack_ = [] 
        for op in operations:
            if op == "C":
                stack_.pop()
            elif op == "D":
                stack_.append(2*int(stack_[-1]))
            elif op == "+":
                stack_.append(int(stack_[-1])+int(stack_[-2]))
            else:
                stack_.append(int(op))
    
        return(sum(stack_)) 