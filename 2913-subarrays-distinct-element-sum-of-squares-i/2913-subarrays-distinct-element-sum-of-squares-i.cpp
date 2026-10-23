class Solution {
public:
    int count(int i , int j, vector<int>& nums) {
        set<int> s;
        for (int l=i; l<=j; l++) {
            s.insert(nums[l]);
        }
        return s.size();
    }
public:
    int sumCounts(vector<int>& nums) {
        int sum=0;
        int n=nums.size();
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                int k=count(i, j, nums);
                sum+=k*k;
            }
        }
        return sum;
    }
};