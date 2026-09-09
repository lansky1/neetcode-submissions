# I was first thinking along the lines of O(n^2) but later thought of a better solution
# Time: 21:57 minutes

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        left = right = 0

        while(right != len(nums)):
            if nums[right] != val:
                if left == right:
                    left, right = left+1, right+1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left, right = left+1, left+1
            else:
                right+=1
        
        return left