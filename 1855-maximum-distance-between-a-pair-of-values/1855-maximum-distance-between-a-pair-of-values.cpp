class Solution {
public:
    int maxDistance(vector<int>& A, vector<int>& B) {
        int n1 = A.size(), n2 = B.size();
        int ptr2 = 0;

        int result = 0;

        for(int i = 0; i < n1; i++) {
            auto it = lower_bound(B.rbegin(), B.rend(), A[i]);
            int pos = n2 - distance(B.rbegin() , it) - 1;
            if (pos > i) result = max(result, pos - i);
        }
        return result;
    }
};