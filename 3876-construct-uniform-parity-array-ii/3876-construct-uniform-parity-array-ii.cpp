class Solution {
public:
    bool uniformArray(vector<int>& A) {
        sort(A.begin(), A.end());

        int oddcnt = 0;
        int eventcnt = 0;

        for (int it: A) {
            if (it % 2 != 0) oddcnt++;
            else eventcnt++;
        }
        if (oddcnt == 0 || eventcnt == 0) return true;

        return A[0] % 2 != 0;
    }
};