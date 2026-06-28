# counter, too much

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        cnt = Counter(nums)
        common = cnt.most_common(2)[0][1]
        return common > 1
