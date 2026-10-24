class Solution {
public:
    int minOperations(auto& s) {
        int n = s.length();
        string temp = s;
        sort(s.begin(), s.end());
        if (temp == s) return 0;
        if (temp[0] == s[0] || temp[n-1] == s[n-1]) return 1;
        if (n == 2){
            if (s[0] != temp[0]) return -1;
        }

        string s1 = temp;
        string s2 = temp;

        sort(s1.begin()+1, s1.end());
        sort(s1.begin(), s1.end() - 1);

        if(s1 == s) return 2;

        sort(s2.begin() , s2.end()-1);
        sort(s2.begin()+1, s2.end());

        if (s2 == s) return 2;
        return 3;
    }
};