# It will scan over all elements, no early exit
# Loop over set is better

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
