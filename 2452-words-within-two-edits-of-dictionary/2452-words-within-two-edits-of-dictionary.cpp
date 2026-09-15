class Solution {
    struct Node {
        vector<Node *> next;
        bool isleaf;

        Node() {
            next = vector<Node *>(26, nullptr);
            isleaf = false;
        }
    };
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        Node *trie = new Node();

        for (string &word : dictionary) {
            Node *temp = trie;
            for (char c : word) {
                int idx = c - 'a';

                if (!temp->next[idx]) temp->next[idx] = new Node();
                temp = temp->next[idx];
            }

            temp->isleaf = true;
        }

        int n = queries.size();
        int i = 0;
        for (int j = 0; j < n; j++) {
            queries[i++] = queries[j];
            if (!cantransform(queries[j], 0, queries[j].size(), trie, 0)) i--;
        }

        queries.resize(i);

        return queries;
    }

    bool cantransform(string &s, int i, int n, Node *root, int errors) {
        if (errors > 2) return false;
        if (i == n) return root->isleaf;

        int idx = s[i] - 'a';
        for (int x = 0; x < 26; x++) {
            if (!root->next[x]) continue;

            bool iserror = (x != idx);
            if (cantransform(s, i + 1, n, root->next[x], errors + iserror)) return true;
        }

        return false;
    }
};