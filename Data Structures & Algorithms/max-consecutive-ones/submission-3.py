'''
    Change: Improve parent loop complexity for n^2 to n
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        i = 0

        while i < len(nums):
            if nums[i] == 1:
                j = i
                while j < (len(nums)-1) and nums[j] != 0:
                    j += 1

                if sum(nums[i:j+1]) > max_count:
                    max_count = sum(nums[i:j+1])

                i = j+1
            else:
                i+=1

        return max_count