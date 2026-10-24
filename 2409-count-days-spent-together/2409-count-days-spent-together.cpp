class Solution {
public:
    set<string> helper(vector<int> d, string arrive, string leave) {
        int cm = stoi(arrive.substr(0 ,2));
        int cd = stoi(arrive.substr(3, 2));

        int em = stoi(leave.substr(0, 2));
        int ed = stoi(leave.substr(3, 2));

        set<string> st;

        while(1) {
            if(cm == 13 || cm > em) break;
            if(cm == em && cd > ed) break;

            string s = to_string(cm) + "." + to_string(cd);
            st.insert(s);

            cd++;
            if(cd > d[cm - 1]) {
                cd = 1;
                cm++;
            }
        }
        return st;
    }
     int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        vector<int> d = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        set<string> st = helper(d, arriveAlice, leaveAlice);
        set<string> st2 = helper(d, arriveBob, leaveBob);

        int ans = 0;
        for(auto i : st){
            if(st2.find(i) != st2.end())ans++; 
        }
        return ans;
    }
};