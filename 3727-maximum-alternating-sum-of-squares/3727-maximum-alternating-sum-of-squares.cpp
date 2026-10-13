#define ll long long
class Solution {
public:
    long long maxAlternatingSum(vector<int>& v) {
        ll ans=0;
        for(int i=0;i<v.size();i++){
            if(v[i]<0){
                v[i]*=-1;
            }
        }
        sort(v.rbegin(),v.rend());
        int n=v.size();
        int till=n/2;
        if(n&1){
            till++;
        }
        for(int i=0;i<till;i++){
            ans+=v[i]*1ll*v[i];
        }
        for(int i=till;i<n;i++){
            ans-=v[i]*1ll*v[i];
        }
        return ans;
        
    }
};