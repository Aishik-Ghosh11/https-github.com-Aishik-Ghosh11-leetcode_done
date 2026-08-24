class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.checker(row):
                print("failed1", row)
                return False
        
        for i in range(9):
            row = [j[i] for j in board]
            if not self.checker(row):
                print("failed2")
                return False
        
        for i in [0, 3, 6]:
            for j in [0 , 3 , 6]:
                row = [y for x in board[i: i+3] for y in x[j:j+3]]
                if not self.checker(row):
                    print("failed3")
                    return False
        return True

    def checker(self, inlist):
        inputlist = [i for i in inlist if i != '.']
        validset = set([str(i) for i in range(1, 10)])
        repeatcheck = len(set(inputlist)) == len(inputlist)
        validcheck = set(inputlist) <= validset
        return repeatcheck and validcheck
        
                
        
