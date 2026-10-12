class Solution {
public:
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        vector<vector<int>> r;
        r.push_back({1, 0});
        for(const auto& elem:restrictions){
            r.push_back({elem[0], elem[1]});
        }
        sort(r.begin(), r.end());
        if(r.back()[0]!=n){
            r.push_back({n, n-1});
        }

        int m=r.size();

        for(int i=1;i<m;i++){
            int dist = r[i][0]-r[i-1][0];
            r[i][1]=min(r[i][1], r[i-1][1]+dist);
        }
        for(int i=m-2;i>=0;i--){
            int dist = r[i+1][0]-r[i][0];
            r[i][1]=min(r[i][1], r[i+1][1]+dist);
        }

        int ans=0;
        for(int i=1;i<m;i++){
            int h1=r[i-1][1];
            int h2=r[i][1];
            int d=r[i][0]-r[i-1][0];
            int candidate = (h1+h2+d)/2;
            ans=max(ans, candidate);
        }
        return ans;
    }
};