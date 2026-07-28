class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        num_spec = 0
        lm = len(mat)
        lr = len(mat[0])
        for row in range(lm):
            for col in range(lr):
                if mat[row][col]:
                    print(f"row: {row}, col: {col}")
                    print(f"any1: {any(mat[row][v] for v in range(lr) if v != col)}")
                    print(f"any2: {any(mat[i][col] for i in range(lm) if i != row)}")
                    if not any(mat[row][v] for v in range(lr) if v != col) and \
                    not any(mat[i][col] for i in range(lm) if i != row):
                        num_spec += 1
        return num_spec











