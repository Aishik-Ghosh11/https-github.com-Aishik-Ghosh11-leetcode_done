class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(),
            [](const auto& a, const auto& b) {
                return a[0] < b[0];
            });


        vector<vector<int>> result;

        for (auto& interval: intervals) {
            if (result.empty() || interval[0] > result.back()[1]) {
            result.push_back(std::move(interval));
        } else {
                result.back()[1] = max(result.back()[1] , interval[1]);
            }
        }
        return result;
    }
};