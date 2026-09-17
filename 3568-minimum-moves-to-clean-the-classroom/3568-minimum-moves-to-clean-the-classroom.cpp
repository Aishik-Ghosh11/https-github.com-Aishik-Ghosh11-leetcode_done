class Solution {
public:
    struct State {
        int x, y, e, mask;
    };

    int minMoves(vector<string>& g, int energy) {
        int m = g.size(), n = g[0].size();

        int sx, sy;
        vector<vector<int>> id(m, vector<int>(n, -1));
        int k = 0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(g[i][j]=='S') sx=i, sy=j;
                if(g[i][j]=='L') id[i][j]=k++;
            }
        }

        int finalMask = (1<<k)-1;

        // visited[x][y][energy][mask]
        vector<vector<vector<vector<int>>>> vis(
            m, vector<vector<vector<int>>>(
                n, vector<vector<int>>(
                    energy+1, vector<int>(1<<k,0)
                )
            )
        );

        queue<pair<State,int>> q;
        q.push({{sx,sy,energy,0},0});
        vis[sx][sy][energy][0]=1;

        int dx[4]={1,-1,0,0};
        int dy[4]={0,0,1,-1};

        while(!q.empty()){
            auto cur=q.front(); q.pop();

            auto [x,y,e,mask]=cur.first;
            int dist=cur.second;

            if(mask==finalMask) return dist;

            for(int d=0;d<4;d++){
                int nx=x+dx[d], ny=y+dy[d];
                if(nx<0||ny<0||nx>=m||ny>=n) continue;
                if(g[nx][ny]=='X') continue;

                int ne=e-1;
                if(ne<0) continue;

                if(g[nx][ny]=='R') ne=energy;

                int nmask=mask;
                if(g[nx][ny]=='L'){
                    nmask |= (1<<id[nx][ny]);
                }

                if(!vis[nx][ny][ne][nmask]){
                    vis[nx][ny][ne][nmask]=1;
                    q.push({{nx,ny,ne,nmask},dist+1});
                }
            }
        }

        return -1;
    }
};