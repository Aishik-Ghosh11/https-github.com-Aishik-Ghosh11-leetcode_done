class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2 or n == 3:
            return 0
        
        used_c = set()
        sum_rc = set()
        diff_rc = set()

        def issafe(r, c, col, dia_1, dia_2):
            if c in used_c or r + c in dia_1 or (r - c) in dia_2:
                return False
            else:
                return True
            
        def backtrack(row):
            if row == n:
                return 1
            
            output = 0
            
            for i in range(n):
                if issafe(row, i, used_c, sum_rc , diff_rc):
                    used_c.add(i)
                    sum_rc.add(row + i)
                    diff_rc.add(row - i)

                    output += backtrack(row + 1)

                    used_c.remove(i)
                    sum_rc.remove(row + i)
                    diff_rc.remove(row - i)
                
            return output
        
        return backtrack(0)

