class Solution {
public:
    int meth(int curr,int prev,vector<int> &a,int &k,vector<vector<int>> &dp)
    {
        if(curr==a.size()-1)
        {
            if(abs(a[curr]-a[prev])<=k)
            return 1;
            return -1e9;
        }
        if(dp[curr][prev]!=-1)
        return dp[curr][prev];
        int take=-1e9;
        if(abs(a[curr]-a[prev])<=k)
        take=1+meth(curr+1,curr,a,k,dp);
        int nottake=meth(curr+1,prev,a,k,dp);
        return dp[curr][prev]=max(take,nottake);
    }
    int maximumJumps(vector<int>& a, int k) {
        int n=a.size();
        vector<vector<int>> dp(n,vector<int>(n,-1e9));
        for(int i=0;i<n-1;i++)
        {
            if(abs(a[i]-a[n-1])<=k)
            dp[n-1][i]=1;
        }
        for(int i=n-2;i>=0;i--)
        {
            for(int j=i-1;j>=0;j--)
            {
                if(abs(a[i]-a[j])<=k)
                dp[i][j]=max(dp[i][j],1+dp[i+1][i]);
                dp[i][j]=max(dp[i][j],dp[i+1][j]);
            }
        }
        return dp[1][0]<0?-1:dp[1][0];
    }
};