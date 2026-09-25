class Solution {
public:

    bool f(int ans,vector<vector<vector<int>>>&adj,vector<bool>&online,long long k){
        priority_queue<vector<long long >,vector<vector<long long>>,greater<vector<long long>>>pq;
        pq.push({0,0,0});
        int n=online.size();
        vector<long long >dis(n,1e15);

        dis[0]=0;
        while(!pq.empty()){
            long long me=pq.top()[1];
            long long d=pq.top()[0];
            long long x=pq.top()[2];
            pq.pop();
            
            if(d>dis[x]){continue;}

            for(auto it:adj[x]){
                if((1ll)*(it[1])<ans || online[it[0]]==false){continue;}
                if(d+(1ll)*(it[1])<dis[it[0]]){
                    dis[it[0]]=d+it[1];
                    pq.push({dis[it[0]],max((1ll)*(it[1]),me),it[0]});
                }
            }
        }
        if(dis[n-1]>k){return false;}
        return true;
    }
    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {

        if(edges.size()==0){return -1;}
        int n=online.size();
        vector<vector<vector<int>>>adj(n);
        set<int>x1;
        vector<int>x;
        for(auto it:edges){
            int u=it[0];
            int v=it[1];
            int c=it[2];
            adj[u].push_back({v,c});
            x1.insert(c);
        }

        for(auto it:x1){
            x.push_back(it);
        }
        int l=0;
        int r=x.size()-1;
        if(!f(x[0],adj,online,k)){return -1;}
        while(r-l>1){
            int mid=(l+r)/2;
            if(f(x[mid],adj,online,k)){
                l=mid;
            }
            else{
                r=mid-1;
            }
        }
        if(f(x[r],adj,online,k)){
            return x[r];
        }
        
        return x[l];  
    }
};