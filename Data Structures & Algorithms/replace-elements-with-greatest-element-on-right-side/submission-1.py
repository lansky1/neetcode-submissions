'''
    iterate backwards, replace with prev max, update max
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_count = -1
        for i in range(len(arr)-1, -1, -1):
            current_element = arr[i]
            arr[i] = max_count
            max_count = max(max_count, current_element)
        
        return arr