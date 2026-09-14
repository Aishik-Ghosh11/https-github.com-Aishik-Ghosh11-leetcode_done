class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        vector<pair<int, int>> a, b;
        int n = img1.size();

        // Store coordinates of 1s
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (img1[i][j])
                    a.push_back({i, j});
                if (img2[i][j])
                    b.push_back({i, j});
            }
        }

        unordered_map<string, int> count;
        int ans = 0;

        // Count possible shifts
        for (auto [x1, y1] : a) {
            for (auto [x2, y2] : b) {
                int dx = x2 - x1;
                int dy = y2 - y1;

                string key = to_string(dx) + "," + to_string(dy);

                count[key]++;
                ans = max(ans, count[key]);
            }
        }

        return ans;
    }
};