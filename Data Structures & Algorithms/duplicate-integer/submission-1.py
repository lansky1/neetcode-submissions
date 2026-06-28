# Using HashSet
# Can Use Counter as well, think syntax

from collections import Counter


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) in (0, 1):
            return False
        cnt = Counter(nums)
        common = cnt.most_common(2)[0][1]
        if common > 1:
            return True
        else:
            return False
