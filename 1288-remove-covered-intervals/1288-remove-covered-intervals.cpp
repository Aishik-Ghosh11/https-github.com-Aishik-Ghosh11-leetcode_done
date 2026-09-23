class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){
            if(a[0] == b[0]) return a[1] > b[1];
            return a[0] < b[0];
        });
        vector<vector<int>> ans;
        for(int i = 0; i < intervals.size(); i++){
            if(i > 0 &&
               ans.back()[0] <= intervals[i][0] &&
               ans.back()[1] >= intervals[i][1]){
                continue;
            }
            ans.push_back(intervals[i]);
        }

        return ans.size();
    }
};