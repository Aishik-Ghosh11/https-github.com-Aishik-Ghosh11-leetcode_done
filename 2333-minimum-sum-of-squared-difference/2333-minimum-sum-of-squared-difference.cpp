class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n = nums1.size();
        // vector<int>dif(n);
        map<int,int>d;
        int mx = 0;
        for(int i = 0;i < n; ++i){
            int temp = abs(nums1[i] - nums2[i]);
            d[temp]++;
            mx = max(mx,temp);
        }
        int k = k1 + k2;
        
        for(int i = mx;i > 0;--i){
            if(k <= 0)break;
            if(d[i] == 0)continue;
            int cost = d[i];
            // return cost;
            if(cost <= k){
                k -= cost;
                d[i-1] += d[i];
                d[i] = 0; 
            }
            else{
                d[i-1] += k;
                d[i] -= k;
                k = 0;
            }
        }
        long long ans = 0;
        for(auto it: d){
            int freq = it.second;
            int dd = it.first;
            ans += 1LL*dd*dd*freq;
        }

        return ans;
        
    }
};