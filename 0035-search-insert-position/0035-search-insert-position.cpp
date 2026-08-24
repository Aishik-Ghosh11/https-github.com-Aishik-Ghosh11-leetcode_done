class Solution {
public:
    int searchInsert(vector<int>& n, int target) {
        int left = 0;
        int right = n.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (n[mid] == target) {
                return mid;
            } else if (n[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};