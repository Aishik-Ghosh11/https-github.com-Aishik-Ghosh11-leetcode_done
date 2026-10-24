class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        int n = nums.size();
        for (int i=0; i<n; i++) {
            pq.push({nums[i], i});
        }
        int i=0;
        vector<int> ans;

        while (!pq.empty() && i<n) {
            auto m=pq.top();
            pq.pop();
            if (m.first == target) {
                ans.push_back(i);
            }
            i++;
        }
        return ans;
    }
};