class Solution {
public:
    long long solve(long long x, vector<int>& coins) {
        int size = coins.size();
        long long sum = 0;
        for (int mask = 1; mask < (1 << size); mask++) {
            int bits = __builtin_popcountll(mask);  
            int64_t leastComMul = 1; 
            for (int j = 0; j < size; j++) {
                if (mask & (1 << j))
                    leastComMul = lcm(leastComMul, coins[j]);
            }
            if (bits & 1)
                sum += x / leastComMul;
            else
                sum -= x / leastComMul;
        }
        return sum;
    }
    long long findKthSmallest(vector<int>& coins, int k) {
        long long l = 0, h = LLONG_MAX, res = 0;
        sort(coins.begin(), coins.end());
        while (l <= h) {
            long long mid = (l + h) / 2;
            if (solve(mid, coins) >= (long long)k) {
                res = mid, h = mid - 1;
            }
            else l = mid + 1;
        }
        return res;
    }
};