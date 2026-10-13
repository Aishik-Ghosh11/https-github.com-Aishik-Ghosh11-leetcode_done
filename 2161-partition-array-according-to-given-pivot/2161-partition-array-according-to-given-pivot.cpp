class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        queue<int> s;
        queue<int> e;

        int cnt = 0;

        for (int i=0; i < nums.size(); i++) {
            if (nums[i] < pivot) {
                s.push(nums[i]);
            }
            else if (nums[i] > pivot) {
                e.push(nums[i]);
            }
            else {
                cnt++;
            }
        }
        int i=0;
        while(!s.empty()) {
            nums[i++] = s.front();
            s.pop();
        }
        while(cnt--) {
            nums[i++] = pivot;
        }
        while(!e.empty()) {
            nums[i++] = e.front();
            e.pop();
        }
        return nums;
    }
};