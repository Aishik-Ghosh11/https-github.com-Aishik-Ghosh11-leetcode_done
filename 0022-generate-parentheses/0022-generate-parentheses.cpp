class Solution {
private:
    bool isValid(string s) {
        int open = 0;
        for (char ch: s) {
            if (ch == '(') open++;
            else {
                open--;
                if (open < 0) return false;
            }
        };
        if (open != 0) return false;
        return true;
    }

public:
    vector<string> generateParenthesis(int n) {
        vector<string> res{};
        for (int i=0; i < 2 << (2 * (n-1)); i++) {
            string s = "";
            int j=i;
            for (int k=0; k<2 * n; k++) {
                if (j % 2 == 1) s += '(';
                else s += ')';
                j = j >> 1;
            };
            if (isValid(s)) res.push_back(s);
        }
        return res;
    }
};