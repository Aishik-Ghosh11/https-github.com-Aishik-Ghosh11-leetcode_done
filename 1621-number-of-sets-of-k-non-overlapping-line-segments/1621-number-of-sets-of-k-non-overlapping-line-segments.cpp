class Solution {
public:
    const int M = 1e9 + 7;
    vector<vector<vector<long long>>> dp;
    long long findans(int i , int j , int k , int n){

        if(i >= n) return j == 0 && k == 0;

        if(j < 0) return 0;

        if(dp[i][j][k] != -1) return dp[i][j][k];

        if(k == 1){
            dp[i][j][k] = findans(i + 1 , j - 1 , 0 , n) + findans(i + 1 , j - 1 , 1 , n) + findans(i + 1 , j , 1 , n);
        }
        else {
            dp[i][j][k] = findans(i + 1 , j , 0 , n) + findans(i + 1 , j , 1 , n);
        }

        return dp[i][j][k] % M;
    }
    int numberOfSets(int n, int k) {

        dp.assign(n , vector<vector<long long>>(k + 1 , vector<long long>(2 , -1)));

        return findans(0 , k , 0 , n) % M;  
    }
};