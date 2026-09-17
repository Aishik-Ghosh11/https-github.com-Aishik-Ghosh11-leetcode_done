class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int totalXor = 0;
        bool hashNonZero = false;

        for(int x : nums) {
            totalXor ^= x;
            if (x != 0) hashNonZero = true;
        }
        int n = nums.size();

        if (totalXor != 0) {
            return n;
        }
        if (hashNonZero) {
            return n-1;
        }
        return 0;
    }
};