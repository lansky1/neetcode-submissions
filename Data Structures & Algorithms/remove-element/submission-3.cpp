/*
    Python for-loop variable stops at n-1 after completion, 
    but C++ increments one final time to n
*/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (size(nums) == 0) return 0;
        int i, j;
        
        for(i = 0; i < size(nums); i++) {
            if(nums[i] == val) {
                j = i;
                while((j < size(nums)-1) and (nums[j]==val)) j++;
                if ((j == size(nums)-1) and (nums[j]==val)) return i;
                else swap(nums[i], nums[j]);
            }
        }
        return i;
    }
};