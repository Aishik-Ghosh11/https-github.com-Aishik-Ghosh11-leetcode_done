class Solution {
public:

    int mod = 1e9 + 7;

    struct Seg{
        long long sqsum = 0, sum = 0, lazy = 0;
        int l, r;

        Seg* left = nullptr;
        Seg* right = nullptr;

        Seg(int l, int r): l(l), r(r) {};
    };

    Seg* root;
    Seg* build(int l , int r){

        if(l > r) return nullptr;

        Seg* ans = new Seg(l, r);
        if(l == r) return ans;

        int m = l + (r - l) / 2;

        ans->left = build(l, m);
        ans->right = build(m+1, r);

        return ans;
    }

    void apply(Seg* nd, long long d){

        if (!nd) return;

        long long k = nd->r - nd->l + 1;

        nd->sqsum = (nd->sqsum + 2LL*d*nd->sum % mod + k*d % mod *d) % mod;

        nd->sum = (nd->sum + k*d) % mod;
        nd->lazy = (nd->lazy + d) % mod;

    }

    void push(Seg* nd){
        if(!nd || !nd->lazy || nd->l == nd->r) return;

        apply(nd->left, nd->lazy);
        apply(nd->right, nd->lazy);

        nd->lazy = 0;
    }

    void upd(int low, int high, Seg* nd){

        if(!nd) return;
        if(nd->l > high || nd->r < low) return;

        int k = nd->r - nd->l + 1;

        if(nd->l >= low && nd->r <= high){
            apply(nd, 1);
            return;
        }

        push(nd);

        upd(low, high, nd->left);
        upd(low, high, nd->right);

        nd->sum = (nd->left->sum + nd->right->sum) % mod;
        nd->sqsum = (nd->left->sqsum + nd->right->sqsum) % mod;

    }

    void print(Seg* nd){

        if(!nd) return;

        cout << nd->l << " " << nd->r << " " << nd->sqsum << " " << nd->sum << "\n";
        print(nd->left);
        print(nd->right);

    }

    int sumCounts(vector<int>& nums) {

        int n = nums.size();
        long long ans = 0;
        root = build(0, n-1);

        unordered_map<int, int> mpp;

        for(int i=0; i<n; i++){
            int x = 0;

            if(mpp.count(nums[i])) x = mpp[nums[i]] + 1;
            upd(x, i, root);

            mpp[nums[i]] = i;

            ans = (ans + root->sqsum) % mod;
        }

        // int ans = 0;
        // print(root);

        return ans;
        
    }
};