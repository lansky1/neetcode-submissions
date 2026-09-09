# I spent significant time thinking about two pointers here. 
# It was much simpler. 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutiveOnes = 0
        count = 0 

        for num in nums:
            if num == 1:
                count+=1
            else:
                maxConsecutiveOnes = max(maxConsecutiveOnes, count)
                count = 0

        return max(maxConsecutiveOnes, count)
