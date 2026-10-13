class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0;
        sort(nums.begin() , nums.end());
        int value = nums[n-1] - nums[0];

        ans = 1LL * value * k;
        return ans;
    }
};