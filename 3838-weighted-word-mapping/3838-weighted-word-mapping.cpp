class Solution {
public:
    int weight(string &s ,vector<int> &weights){
         int n = s.size();
         int totalWeight = 0;
         for(int i = 0 ; i < n ; i++){
               int currCharVal = s[i] - 'a';
               totalWeight += weights[currCharVal];
         }

         return totalWeight;
    }
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
         string ans = "";
         for(auto it : words){
             int totalWeight = weight(it , weights);
             totalWeight = totalWeight%26;
              ans.push_back('z' - totalWeight);
         }

        return ans;
    }
};