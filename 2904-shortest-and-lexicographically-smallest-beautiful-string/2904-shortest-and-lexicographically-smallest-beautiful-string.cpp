class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();
        vector<string>ans;
        int  mini = 1e9;
        for(int i=0; i<n; i++) {
            int count = 0;
            string temp;
            for(int j = i; j<n; j++) {
                if(s[j]=='1') count++;
                if(count<=k) temp+=s[j];
                if(count==k){
                    ans.push_back(temp);
                    mini = min(mini, j-i+1);
                }
            }
        }
        sort(ans.begin() , ans.end());
        for(auto x: ans) {
            if(x.size()==mini) return x;
        }
        return "";
    }
};