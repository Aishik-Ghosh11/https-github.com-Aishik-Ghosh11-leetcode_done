class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int sum = nums[0];

        // Find the longest sequential prefix
        int i = 1;
        while (i < nums.size() && nums[i] == nums[i - 1] + 1) {
            sum += nums[i];
            i++;
        }

        // Store all numbers in a hash set
        unordered_set<int> st(nums.begin(), nums.end());

        // Find the smallest missing integer >= sum
        while (st.count(sum)) {
            sum++;
        }
        return sum;
    }
};



