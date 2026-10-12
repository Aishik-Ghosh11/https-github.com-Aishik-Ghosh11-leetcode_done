/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* temp = head;
        int n = 0;
        while(temp) {
            n++;
            temp = temp->next;
        }
        temp = head;
        vector<int> res(n, 0);
        int idx = 0;
        while (temp) {
            int twin = n-1-idx;
            int i = min(idx, twin);
            res[i] += temp->val;
            idx++;
            temp = temp->next;
        }
        return *max_element(res.begin(), res.end());
    }
};