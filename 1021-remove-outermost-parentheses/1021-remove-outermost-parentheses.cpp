class Solution {
public:
    string removeOuterParentheses(string s) {
        unordered_set<int> idxs;
        int len = 0, n = s.size();
        for(int i = 0; i < n; i++){
            if(len==0)
                idxs.insert(i);
            s[i]=='(' ? len++ : len--;
            if(len==0)
                idxs.insert(i);
        }
        string res = "";
        for(int i = 0; i < n; i++)
            idxs.find(i)==idxs.end() ? res += s[i] : res;
        return res;
    }
};