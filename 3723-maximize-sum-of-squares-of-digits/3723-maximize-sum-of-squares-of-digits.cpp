class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        int k=0;
        string ans = "";
        while (sum > 0) {
            for (int i=9; i >= 1; i--) {
                if (sum >= i) {
                    sum -= i;
                    ans += to_string(i);
                    break;
                }
            }
            k++;
            if (k == num) break;
        }
        cout<<ans<<endl;
        if (sum > 0) {
            return "";
        }
        if (sum > 0) {
            return "";
        }
        if (k < num) {
            for (int i=k; i < num ; i++) {
                ans += "0";
            }
        }
        return ans;
    }
};