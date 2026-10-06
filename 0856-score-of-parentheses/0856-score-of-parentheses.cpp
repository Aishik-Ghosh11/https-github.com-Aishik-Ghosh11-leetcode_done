class Solution {
public:
    int scoreOfParentheses(string s) {
        
        int n = s.size();
        // -1: uninitialized, -2: invalid
        vector<vector<int>> dp(n, vector<int>(n, -1));

        auto score = [&](auto &&self, int i, int j) -> int {
            if (dp[i][j] != -1) return dp[i][j];
            if (i + 1 == j) {
                if (s[i] == '(' && s[j] == ')') return dp[i][j] = 1;
                else return dp[i][j] = -2;
            }
            if (s[i] == '(' && s[j] == ')') {
                int s = self(self, i+1, j-1);
                if (s != -2) return dp[i][j] = 2 * s;
            }
            for (int x = i+1; x <= j-2; ++x) {
                int a = self(self, i, x);
                int b = self(self, x+1, j);
                if (a != -2 && b != -2) return dp[i][j] = a + b;
            }
            return dp[i][j] = -2;
        };

        return score(score, 0, s.size()-1);
    }
};