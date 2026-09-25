class Solution {
    struct Node {
        Node* c[26]{};
        Node* f{};
        Node* l{};
        int n = 0;
    };

    static constexpr int mx = 10005;

public:
    int numOfStrings(vector<string>& patterns, string word) {
        Node* root = new Node();

        for (auto& p : patterns) {
            Node* curr = root;
            for (int i = 0; i < p.size(); i++) {
                int x = p[i] - 97;
                if (!curr->c[x]) {             
                    curr->c[x] = new Node();   
                }
                curr = curr->c[x];
            }
            curr->n++;
        }

        Node* q[mx];
        int hd = 0;
        int tl = 0;

        for (int i = 0; i < 26; i++) {
            if (!root->c[i]) {
                root->c[i] = root;
                continue;
            }
            root->c[i]->f = root;
            root->c[i]->l = nullptr;
            q[tl++] = root->c[i];
        }

        while (hd < tl) {
            Node* curr = q[hd++];
            for (int i = 0; i < 26; i++) {
                if (!curr->c[i]) {
                    curr->c[i] = curr->f->c[i];
                } else {
                    Node* child = curr->c[i];
                    child->f = curr->f->c[i];
                    child->l = (child->f->n > 0) ? child->f : child->f->l;
                    q[tl++] = child;
                }
            }
        }

        int ans = 0;
        Node* curr = root;
        for (char ch : word) {
            curr = curr->c[ch - 97];
            for (Node* temp = curr; temp != nullptr; temp = temp->l) {
                if (temp->n > 0) {
                    ans += temp->n;
                    temp->n = 0; 
                }
            }
        }

        return ans;
    }
};