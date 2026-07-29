class Solution {
public: 
    // Added prefSum as a parameter
    int funct(vector<int>& nums, vector<int>& prefSum, int L, int M){
        int n = nums.size();
        int maxLeftSubSum = 0;
        int result = 0; // Max Sum

        for(int mEnd = L + M - 1; mEnd < n; mEnd++){
            int lEnd = mEnd - M;
            int lStartPrev = lEnd - L;

            // Fixed spelling mistakes in variable names
            int mBlockSum = prefSum[mEnd] - prefSum[lEnd];
            int lBlockSum = prefSum[lEnd] - (lStartPrev < 0 ? 0 : prefSum[lStartPrev]);

            maxLeftSubSum = max(maxLeftSubSum, lBlockSum);

            // Added the missing semicolon
            result = max(result, maxLeftSubSum + mBlockSum);
        }
        return result;
    }
    
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();

        vector<int> prefSum(n, 0);
        prefSum[0] = nums[0];
        for(int i = 1; i < n ; i++){
            prefSum[i] = prefSum[i-1] + nums[i];
        }

        // Passed prefSum to funct and updated variables to match the function parameters
        return max(funct(nums, prefSum, firstLen, secondLen), 
                   funct(nums, prefSum, secondLen, firstLen));
    }
};