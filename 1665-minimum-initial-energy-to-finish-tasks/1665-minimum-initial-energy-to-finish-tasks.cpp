class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        std::ranges::sort(tasks, [](const auto & lhs, const auto & rhs) {
            return max(lhs[1], lhs[0] + rhs[1]) < max(rhs[1], rhs[0] + lhs[1]);
        });

        int ans = 0, cur = 0;
        for (const auto & task: tasks) {
            int act = task[0], mn = task[1];
            if (cur < mn) {
                ans += mn - cur;
                cur = mn;
            }
            cur -= act;
        }
        return ans;
    }
};