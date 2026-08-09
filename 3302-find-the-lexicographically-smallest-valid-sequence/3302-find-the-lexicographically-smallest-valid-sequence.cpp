class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.length();
        int m = word2.length();
        
        // Step 1: Precompute the longest suffix match 
        // rightHandSideLength[i] will store the maximum length of a suffix 
        // of word2 that can be found as a subsequence in word1[i...n-1]
        vector<int> rightHandSideLength(n + 1, 0);
        int j = m - 1;
        for (int i = n - 1; i >= 0; --i) {
            if (j >= 0 && word1[i] == word2[j]) {
                rightHandSideLength[i] = rightHandSideLength[i + 1] + 1;
                j--;
            } else {
                rightHandSideLength[i] = rightHandSideLength[i + 1];
            }
        }
        
        // Step 2: Greedy approach to find the lexicographically smallest indices
        vector<int> seq;
        bool changePower = true; // can change only one character
        j = 0;
        
        for (int i = 0; i < n && j < m; ++i) {
            if (word1[i] == word2[j]) {
                seq.push_back(i);
                j++;
            } 
            else if (changePower && rightHandSideLength[i + 1] >= m - j - 1) {
                // We use our changePower here because picking an earlier index 'i' 
                // guarantees a lexicographically smaller sequence.
                seq.push_back(i);
                j++;
                changePower = false;
            }
        }
        
        // If we successfully matched all characters of word2, return the sequence
        if (seq.size() == m) {
            return seq;
        }
        
        return {};
    }
};