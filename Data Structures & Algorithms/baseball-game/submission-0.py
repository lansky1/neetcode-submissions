class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        finalScore = 0
        numElements = 0

        for op in operations:
            if op == "+":
                newScore = scores[numElements-1]+scores[numElements-2]
                scores.append(newScore)
                finalScore+=newScore
                numElements+=1
            elif op == "D":
                newScore = scores[numElements-1]*2
                scores.append(newScore)
                finalScore+=newScore
                numElements+=1
            elif op == "C":
                finalScore-=scores[numElements-1]
                numElements-=1
                scores.pop()
            else:
                scores.append(int(op))
                numElements+=1
                finalScore+=int(op)

        return finalScore