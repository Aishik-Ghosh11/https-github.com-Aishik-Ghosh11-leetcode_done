class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        vector<int> arr = nums;
        sort(arr.begin(), arr.end());
        int n = arr.size();
        int val = INT_MAX;
        for (int i=0; i<n; i++) {
            if (arr[i] != nums[i])
                val = val & nums[i];
        }
        return val == INT_MAX?0:val;
    }
};