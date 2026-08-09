class Solution {
public:
    vector<int> validSequence(string s, string t) {
        int n=s.size() ,m=t.size();

        vector<int> dp(n+1), ans;

        int j=m-1;
        bool ok = 1;

        for(int i=n-1; i>=0 ;i--) {
            dp[i] = dp[i+1];

            if(j>=0&&s[i]==t[j]) {
                j--;
                dp[i]++;
            }
        }

        j=0;

        for(int i=0; i<n&&j<m;i++){
            if(s[i]==t[j]) {
                ans.push_back(i);
                j++;
            } else if(ok&&dp[i+1]>=m-j-1){
                ans.push_back(i);
                ok=0;
                j++;
            }
        }
        return ans.size()==m?ans:vector<int>{};
    }
};