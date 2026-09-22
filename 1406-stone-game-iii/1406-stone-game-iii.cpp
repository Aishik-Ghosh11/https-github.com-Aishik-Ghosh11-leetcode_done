class Solution {
public:
    string stoneGameIII(vector<int>& A) {
        int n = A.size();
        vector<vector<int>> dp(n + 1, vector<int>(2, 0));

        for (int i=n-1; i >= 0; i--) {
            for (int p=0; p <= 1; p++) {
                int moveScore = 0;
                dp[i][p] = p ? INT_MIN : INT_MAX;
                for (int j=i; j <= min(i + 2, n-1); j++) {
                    moveScore += A[j];
                    if (p) dp[i][1] = max(dp[i][1], dp[j+1][0] + moveScore);
                    else dp[i][0] = min(dp[i][0], dp[j + 1][1] - moveScore);
                }
            }
        }
        return dp[0][1] > 0 ? "Alice" : dp[0][1] < 0 ? "Bob" : "Tie";
    }
};