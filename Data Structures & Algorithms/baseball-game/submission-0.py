class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack_ = [] 
        for op in operations:
            try:
                num = int(op)
            except:
                if op == "C":
                    stack_.pop()
                elif op == "D":
                    stack_.append(2*stack_[-1])
                elif op == "+":
                    stack_.append(stack_[-1]+stack_[-2])
                else:
                    pass
            else:
                stack_.append(num)
    
        return(sum(stack_)) 