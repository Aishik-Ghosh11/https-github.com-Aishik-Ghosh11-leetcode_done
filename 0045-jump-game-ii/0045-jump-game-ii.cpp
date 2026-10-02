class Solution {
public:
    vector<int> memo;
    int helper(vector<int>& nums , int index){

        if(index == nums.size()-1) return 0;
        if(index >= nums.size()) return 1e9;

        if(memo[index] != -1) return memo[index];

        int minJump = 1e9;
         
        for(int i=1 ; i <= nums[index] ; i++){
            minJump = min(minJump , 1 + helper(nums,index+i));
        }

        return memo[index] = minJump;
    }
    int jump(vector<int>& nums) {
        memo.assign(nums.size(),-1);
        return helper(nums,0);
    }
};
