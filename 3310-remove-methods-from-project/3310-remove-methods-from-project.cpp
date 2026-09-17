class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> adj(n);

        for(auto& e : invocations) adj[e[0]].push_back(e[1]);
        vector<char> sus(n, 0);
        vector<int> stk = {k};
        sus[k] = 1;
        while (!stk.empty()) {
            int u = stk.back(); stk.pop_back();
            for (int v: adj[u]) if (!sus[v]) {sus[v] = 1; stk.push_back(v); }
        }
        for (auto& e: invocations) {
            if (!sus[e[0]] && sus[e[1]]) {
                vector<int> res(n);
                for (int i = 0 ; i < n; i++) res[i] = i;
                return res;
            }
        }
        vector<int> res;
        for(int i=0; i<n; i++) if (!sus[i]) res.push_back(i);
        return res;
    }
};