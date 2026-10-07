#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    set<string> ans;

    void dfs(string &s, int idx, int leftRem, int rightRem,
             int balance, string cur) {

        if (idx == s.size()) {
            if (leftRem == 0 && rightRem == 0 && balance == 0)
                ans.insert(cur);
            return;
        }

        // Remove current parenthesis
        if (s[idx] == '(' && leftRem > 0) {
            dfs(s, idx + 1, leftRem - 1, rightRem,
                balance, cur);
        }

        if (s[idx] == ')' && rightRem > 0) {
            dfs(s, idx + 1, leftRem, rightRem - 1,
                balance, cur);
        }

        // Keep current character
        if (s[idx] == '(') {
            dfs(s, idx + 1, leftRem, rightRem,
                balance + 1, cur + '(');
        }
        else if (s[idx] == ')') {
            if (balance > 0) {
                dfs(s, idx + 1, leftRem, rightRem,
                    balance - 1, cur + ')');
            }
        }
        else {
            dfs(s, idx + 1, leftRem, rightRem,
                balance, cur + s[idx]);
        }
    }

    vector<string> removeInvalidParentheses(string s) {

        int leftRem = 0;
        int rightRem = 0;

        // Find minimum removals required
        for (char c : s) {

            if (c == '(') {
                leftRem++;
            }
            else if (c == ')') {

                if (leftRem > 0)
                    leftRem--;
                else
                    rightRem++;
            }
        }

        dfs(s, 0, leftRem, rightRem, 0, "");

        return vector<string>(ans.begin(), ans.end());
    }
};