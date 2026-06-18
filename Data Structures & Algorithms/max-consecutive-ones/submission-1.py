class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                j = i
                while j < len(nums) and nums[j] != 0:
                    j += 1

                if sum(nums[i:j]) > max_count:
                    max_count = sum(nums[i:j])

        return max_count