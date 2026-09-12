class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return pairs

        stepList = [pairs.copy()]
        for i in range(1, len(pairs)):
            key = pairs[i]
            j = i-1
            while(j >= 0 and pairs[j].key>key.key):
                pairs[j+1] = pairs[j]
                j-=1
            pairs[j+1] = key
            stepList.append(pairs.copy())
            
        return stepList
