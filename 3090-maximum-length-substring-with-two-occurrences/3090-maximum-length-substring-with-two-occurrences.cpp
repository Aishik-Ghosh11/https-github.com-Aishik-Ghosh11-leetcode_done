class Solution {
public:
    int maximumLengthSubstring(string s) {
        int n = s.size();
        int mx = 0;

        unordered_map<char, int> mp;
        for(int i = 0; i < n; i++) {
            unordered_map<char, int> freq;
            for(int j = i; j < n; j++) {
                freq[s[j]]++;
                if(freq[s[j]] > 2)break;
                mx = max(mx, j-i+1);
            }
        }
        return mx;
    }
};