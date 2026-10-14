class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n=nums.size();
        vector<int> answer(n);
        for (int i=0; i<n; i++) {
            int Lsum = 0;
            int Rsum = 0;
            for (int j=0; j<i; j++) {
                Lsum += nums[j];
            }
            for (int j=i+1 ; j<n ; j++) {
                Rsum += nums[j];
            }
            answer[i] = abs(Lsum - Rsum);
        }
        return answer;
    }
};