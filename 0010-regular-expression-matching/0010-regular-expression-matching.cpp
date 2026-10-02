class Solution {
public:
    bool help(int i , string &s , int j , string & p ){
        if (i==s.size() && j==p.size()) return true ;
        if (j==p.size()) return false ;

        if (i==s.size()){
            while(j+1<p.size() && p[j+1]=='*') j+=2;
            if (j==p.size()) return true;
            return false;
        }

        if (j+1<p.size() && p[j+1]=='*'){
            bool skip =help(i, s, j+2, p);
            bool take=false ;
            if (s[i]==p[j] || p[j]=='.' )  take=help(i+1, s, j , p);
            return skip||take;
        }
        if (s[i]==p[j] || p[j]=='.') return help(i+1  , s, j+1 , p);

        return false ;
    }
    bool isMatch(string s, string p) {
        return help(0 , s, 0 , p);
    }
};