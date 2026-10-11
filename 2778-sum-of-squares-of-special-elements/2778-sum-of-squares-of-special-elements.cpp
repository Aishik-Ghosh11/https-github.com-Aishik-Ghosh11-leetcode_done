class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        vector<int> special;
        for (int i=0; i<nums.size(); i++) {
            if (nums.size()%(i + 1) == 0) {
                special.push_back(nums[i]);
            }
        }
        int sum=0;
        for (int x: special) {
            int sqr = x*x;
            sum += sqr;
        }
    return sum;
    }
};