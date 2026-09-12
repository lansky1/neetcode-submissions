class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countArray = [0] * 3
        for num in nums:
            countArray[num] += 1

        idx = 0
        for i in range(len(countArray)):    
            for _ in range(countArray[i]):  
                nums[idx] = i  
                idx+=1               
