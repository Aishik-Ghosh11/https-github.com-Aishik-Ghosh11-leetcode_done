class Solution {
public:
    bool isValid3x3( vector<vector<char>>& board, int l, int r ){
        unordered_set<char> st;
        for(int i=l; i<l+3; i++){
            for(int j=r; j<r+3; j++){
                if( board[i][j] != '.' && st.find(board[i][j]) != st.end() ){
                    cout << "3 I returned here i : " << i << " j: " << j << endl;
                    cout << board[i][j];
                    return false;
                }
                st.insert( board[i][j] );
            }
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i=0; i<9; i++){
            unordered_set<char> hst;
            unordered_set<char> st;
            for(int j=0; j<9; j++){
                if( board[i][j] != '.' && st.find(board[i][j]) != st.end() ){
                    cout << "1 I returned here i : " << i << " j: " << j << endl;
                    cout << board[i][j];
                    return false;
                }
                if( board[j][i] != '.' && hst.find(board[j][i]) != hst.end() ){
                    cout << "2 I returned here i : " << i << " j: " << j << endl;
                    cout << board[j][i];
                    return false;
                }
                hst.insert(board[j][i]);
                st.insert(board[i][j]);
            }
        }
        for(int i=0; i<9; i+=3){
            for(int j=0; j<9; j+=3){
                if(!isValid3x3(board, i, j)) return false;
            }
        }
        return true;
    }
};