class Solution {
public:
    int helper(vector<int>& nums, int& firstLen, int secondLen, int st, int end, 
    vector<vector<int>>& dp) {
        if(firstLen == -1) {
            return 0;
        }

        if(dp[st][end] != -1) {
            return dp[st][end];
        }

        int result = 0;
        int sum = 0;

        for (int i = 0, j = 0; j < nums.size(); j++) {
            if (j == st) {
                j = end + 1;
                i = end + 1;
                sum = 0;
                if(j >= nums.size()) break;
            }

            sum += nums[j];

            if ((j - i + 1) == firstLen) {
                int secondLenMax = helper(nums, secondLen, -1, i, j, dp);
                dp[i][j] = result = max(sum + secondLenMax, result);
                sum -= nums[i];
                i++;
            }
        }

        return result;
    }

    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();
        vector<vector<int>> dp(n+1, vector<int>(n+1, -1));

        return helper(nums, firstLen, secondLen, n, n, dp);
    }
};