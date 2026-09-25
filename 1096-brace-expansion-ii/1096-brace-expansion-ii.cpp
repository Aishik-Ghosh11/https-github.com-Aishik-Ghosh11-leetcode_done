class Solution {
public:
    vector<string> braceExpansionII(string expression) {
        set<string> result = parse(expression);
        return vector<string>(result.begin(), result.end());
    }

private:
    set<string> parse(string s) {
        stack<set<string>> st;
        stack<char> ops;
        int n = s.size();

        for (int i = 0; i < n; ++i) {
            if (isalpha(s[i])) {
                set<string> cur = {string(1, s[i])};
                st.push(cur);
            } else if (s[i] == '{') {
                ops.push('{');
            } else if (s[i] == '}') {
                while (!ops.empty() && ops.top() != '{') {
                    merge(st, ops.top());
                    ops.pop();
                }
                ops.pop(); // remove '{'
            } else if (s[i] == ',') {
                while (!ops.empty() && ops.top() == '*') {
                    merge(st, ops.top());
                    ops.pop();
                }
                ops.push('+');
            }

            // implicit concatenation
            if (i + 1 < n && (isalpha(s[i]) || s[i] == '}') &&
                (isalpha(s[i + 1]) || s[i + 1] == '{')) {
                ops.push('*');
            }
        }

        while (!ops.empty()) {
            merge(st, ops.top());
            ops.pop();
        }

        return st.top();
    }

    void merge(stack<set<string>>& st, char op) {
        auto b = st.top(); st.pop();
        auto a = st.top(); st.pop();
        set<string> res;

        if (op == '+') {
            res = a;
            res.insert(b.begin(), b.end());
        } else if (op == '*') {
            for (auto& x : a)
                for (auto& y : b)
                    res.insert(x + y);
        }

        st.push(res);
    }
};