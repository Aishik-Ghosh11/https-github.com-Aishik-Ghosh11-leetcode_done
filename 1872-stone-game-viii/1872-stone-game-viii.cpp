class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int n = stones.size();
        vector<int> pref(n);
        
        // 1. Calculate prefix sums
        pref[0] = stones[0];
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i-1] + stones[i];
        }
        
        // 2. Base case: If forced to take the last stone, the score difference is just pref[n-1]
        int dp = pref[n-1];
        
        // 3. Work backward from the second-to-last choice down to the first valid choice (x > 1, so i = 1)
        for (int i = n - 2; i >= 1; i--) {
            dp = max(dp, pref[i] - dp);
        }
        
        return dp;
    }
};