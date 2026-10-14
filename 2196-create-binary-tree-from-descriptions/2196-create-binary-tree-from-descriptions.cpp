/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right)
 *         : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        int n = descriptions.size();
        map<int, TreeNode*> mpp;
        set<int> isNotRoot;

        for(auto it : descriptions){
            int parent = it[0];
            int child = it[1];
            int isLeft = it[2];

            isNotRoot.insert(child);

            if(mpp.find(parent) == mpp.end()) {
                TreeNode* node = new TreeNode(parent);
                mpp[parent] = node;
            }

             if(mpp.find(child) == mpp.end()) {
                TreeNode* node = new TreeNode(child);
                mpp[child] = node;
            }

            if(isLeft) {
                mpp[parent]->left = mpp[child];
            } else mpp[parent]->right = mpp[child];
        }

        
        for(int i=0;i<n;i++) {
            if(isNotRoot.find(descriptions[i][0]) == isNotRoot.end()){
                return mpp[descriptions[i][0]];
            }
        }

        return nullptr;
    }
};