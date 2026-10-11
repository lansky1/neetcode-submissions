class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for idx, num in enumerate(nums):
            if target-num in numbers:
                return [numbers[target-num],idx]
            numbers[num] = idx
