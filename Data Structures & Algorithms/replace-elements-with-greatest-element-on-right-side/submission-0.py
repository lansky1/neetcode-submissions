# Time: 8 minutes

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prevMax = currMax = -1
        
        for i in range(len(arr)-1, -1, -1):
            currMax = max(currMax, arr[i])
            arr[i] = prevMax
            prevMax = max(prevMax, currMax)

        return arr