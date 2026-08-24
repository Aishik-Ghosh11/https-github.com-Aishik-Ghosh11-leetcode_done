class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();

        int ans = 0;
        for(int i=0; i<n; i++) {
            if(nums[i]==target) {
                ans=i;
                return ans;
            } 
        }
        nums.push_back(target);
        int a=nums.size();
        sort(nums.begin(), nums.end());
        for(int i=0; i<a; i++){
            if(nums[i]==target){
                ans=i;
            }
        }
        return ans;
    }
};