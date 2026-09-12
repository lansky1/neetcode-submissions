# If duplicate is found, it doesnt process further. 
# Better than len(nums) and len(set(nums))

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False
