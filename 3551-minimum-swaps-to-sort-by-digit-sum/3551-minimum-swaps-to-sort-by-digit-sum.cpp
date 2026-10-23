class Solution {
public:
    constexpr int dSum(int n) {
        int s = 0;
        while (n > 0) {
            s += n % 10;
            n /= 10;
        }
        return s;
    }
    int minSwaps(vector<int>& nums) {
        const int n = nums.size();
        vector<int> order(n), sum(n);
        iota(order.begin(), order.end(), 0);

        for (int i=0; i < n; i++) {
            sum[i] = dSum(nums[i]);
        }
        ranges::sort(order, {}, [&](int i){
            return pair{sum[i], nums[i]};
        });

        int swaps = 0;

        for (int i=0; i < n; i++) {
            while (order[i] != i) {
                int j = order[i];
                swap(order[i], order[j]);
                swaps++;
            }
        }
        return swaps;
    }
};