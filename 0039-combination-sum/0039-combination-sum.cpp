class Solution {
public:
    vector<vector<int>> ans;
    void solve(vector<int> nums,int target,int i,vector<int> temp) {

        if(target==0) {
            ans.push_back(temp);
            return;
        }
        if(i==nums.size()||target<0) {
            return;
        }
        if(nums[i]<=target) {
            temp.push_back(nums[i]);
        solve(nums,target-nums[i],i,temp);
        temp.pop_back();
        }
        
        solve(nums,target,i+1,temp);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        solve(candidates,target,0,temp);

        return ans;
    }
};