'''
    Iterate over each element
    For each element i, iterate from i+1 to end, 
    store the max element
    once end is reached, swap ith element with max
    once you are at end, replace that with -1
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[-1] = -1
            else:
                max_element = 0
                for j in range(i+1, len(arr)):
                    max_element = max(max_element, arr[j])
                arr[i] = max_element
        
        return arr