"""
It is a question of who reaches end first - i or j
if i reaches, return i+1
otherwise i
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if nums[i] == val:
                j = i
                while j < len(nums)-1 and nums[j] == val:
                    j += 1
                if j == len(nums) - 1 and nums[j]==val:
                    return i
                else:
                    nums[i], nums[j] = nums[j], nums[i]

        if i == len(nums) - 1:
            return i + 1
