class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> newNums(2*size(nums));
        for(int i = 0; i<size(nums); i++) {
            newNums[i] = nums[i];
        }
        for(int i = 0; i<size(nums); i++) {
            newNums[size(nums)+i] = nums[i];
        }
        return newNums;
    }
};