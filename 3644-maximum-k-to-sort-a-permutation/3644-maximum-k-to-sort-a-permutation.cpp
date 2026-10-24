class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        vector<int> temp;
        for(int i=0; i<nums.size(); i += 1) {
            if (nums[i] != i) {
                temp.push_back(nums[i]);
            }
        }
        
        int ans = 0;
        vector<int> sbits(32 , 0);
        for (int i=0; i < temp.size(); i++) {
            for(int j=0; j < 31; j++) {
                if((1 << j) & temp[i]) {
                    sbits[j] += 1;
                }
            }
        }
        if(temp.size() == 0) return 0;

        for(int i=0;i<32;i+=1){
            if(sbits[i]==temp.size()){
                ans+=(1<<i);
            }
        }

        return ans;
    }
};