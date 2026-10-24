class Solution {
public:
    bool kmp(vector<int>& vec1, vector<int>& text) {
    int m = vec1.size();
    if (m == 0) return true;

    vector<int> lps(m, 0);

    for (int i = 1, j = 0; i < m; ) {
        if (vec1[i] == vec1[j]) {
            lps[i++] = ++j;
        } else if (j > 0) {
            j = lps[j - 1];
        } else {
            lps[i++] = 0;
        }
    }

    for (int i = 0, j = 0; i < (int)text.size(); ) {
        if (text[i] == vec1[j]) {
            ++i;
            ++j;
            if (j == m) return true;
        } else if (j > 0) {
            j = lps[j - 1];
        } else {
            ++i;
        }
    }

    return false;
}

bool isrotation(vector<int>& vec1, vector<int>& vec2) {
    if (vec1.size() != vec2.size()) return false;

    vector<int> text;
    text.reserve(2 * vec2.size());
    text.insert(text.end(), vec2.begin(), vec2.end());
    text.insert(text.end(), vec2.begin(), vec2.end());

    return kmp(vec1, text);
}
    int sortableIntegers(vector<int>& nums) {
        int n=nums.size();
        vector<int>sorted=nums;
        sort(begin(sorted),end(sorted));
        int res=0;
        for(int k=1;k<=n;k++){
            if(n%k!=0) continue;
            bool valid=true;
            for(int start=0;start<n;start+=k){
                vector<int>vec1(begin(nums)+start,begin(nums)+start+k);
                vector<int>vec2(begin(sorted)+start,begin(sorted)+start+k);
                if(!isrotation(vec1,vec2)){
                    valid=false;
                    break;
                }
            }
            if(valid) res+=k;
        }
        return res;
    }
};