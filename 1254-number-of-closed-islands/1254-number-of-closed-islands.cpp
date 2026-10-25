class Solution {
public:
    void bfs(int i, int j, vector<vector<int>>&vis, vector<vector<int>>&grid){
        int m = grid.size();
        int n = grid[0].size();

        queue<pair<int, int>>q;
        q.push({i, j});
        vis[i][j] = 1;

        while(!q.empty()){
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            vis[r][c] = 1;
            int dr[] = {0, 0, 1, -1};
            int dc[] = {1, -1, 0, 0};

            for(int k=0; k<4; k++){
                int nr = r + dr[k];
                int nc = c + dc[k];

                if(nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0 && !vis[nr][nc]){
                    q.push({nr, nc});
                }
            }
        }
    }
    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>>vis(m, vector<int>(n, 0));
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if((i==0 || i == m-1 || j == 0 || j == n-1) && grid[i][j] == 0 && vis[i][j] == 0){
                    bfs(i, j, vis, grid);
                }
            }
        }
        int count = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 0 && vis[i][j] == 0){
                    bfs(i, j, vis, grid);
                    count++;
                }
            }
        }
        return count;
    }
};