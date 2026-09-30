class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> comb;
        dfs(0, res, 0, target, comb, candidates);
        return res;
    }
    void dfs(int i, vector<vector<int>>& res, int sum, int target, vector<int>& comb, vector<int>& candidates) {
        if(sum==target) {
            res.push_back(comb);
            return;
        }
        if(i>=candidates.size() || sum>target) {
            return;
        }
        comb.push_back(candidates[i]);
        dfs(i, res, sum+candidates[i], target, comb, candidates);
        comb.pop_back();
        dfs(i+1, res, sum, target, comb, candidates);
    }
};