class Solution {
public:
    vector<int> maxDepthAfterSplit(string s) {
        int curr = 0, ans = 0;
        vector<int> v;
        for (int i=0; i < s.size(); i++) {
            if (s[i] == '(') curr++;
            if (s[i] == ')') curr--;

            ans = max(ans, curr);
        }

        curr = 0; ans = (ans + 1) / 2;
        for (int i=0; i < s.size(); i++) {
            if (s[i] == '(') curr++;
            if (curr <= ans) v.push_back(0);
            else v.push_back(1);
            if (s[i] == ')') curr--;
        }

        return v;

    }
};