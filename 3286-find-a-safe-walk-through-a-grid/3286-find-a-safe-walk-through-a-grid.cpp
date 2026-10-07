class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m=grid.size();
        int n=grid[0].size();
        vector<vector<int>>vec(m,vector<int>(n,-1));
        queue<vector<int>>q;
        if(grid[0][0]>=health) return false;
        int safe=health-grid[0][0];
        vec[0][0]=safe;
        int dx[] ={0,0,1,-1};
        int dy[] ={-1,1,0,0};
        q.push({0,0,safe});
        while(!q.empty()){
            auto curr=q.front();
            q.pop();
            int x=curr[0];
            int y=curr[1];
            int he=curr[2];
            if(x==m-1 && y==n-1) return true;
            for(int i=0;i<4;i++){
                int rx=x+dx[i];
                int cx=y+dy[i];
                if(rx<0 || rx>=m || cx<0 || cx>=n) continue;
                int h=he-grid[rx][cx];
                if(h<=0) continue;
                if(vec[rx][cx]>=h) continue;
                vec[rx][cx]=h;
                q.push({rx,cx,h});
            }
        }
        return false;
    }
};