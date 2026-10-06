class Solution {
public:
    bool find(string &s, int ind, int state, map<pair<int, int>,bool>&m){
        if (ind == s.size()) {
            return !state;
        }
        if(m.find({state, ind}) != m.end()) return m[{state, ind}];
        if (s[ind] == '(') {
            if (find(s, ind + 1, state + 1, m)) return true;
        } else if (s[ind] == ')') {
            if(!state) return false;
            if(find(s, ind + 1, state - 1, m)) return true;
        }
        else {
            if (find(s, ind + 1, state + 1, m)) return true;
            if (find(s , ind + 1, state, m)) return true;
            if (state) {
                if (find(s , ind + 1, state - 1, m)) return true;
            }
        }
        m[{state, ind}] = false;
        return false;
    }
    bool checkValidString(string s) {
        map<pair<int, int>, bool>m;
        if (find(s, 0, 0, m)) return true;
        return false;
    }
};