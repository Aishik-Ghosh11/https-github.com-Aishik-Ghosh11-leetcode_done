class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dikt = {}
        for r, s in reservedSeats:
            if r not in dikt:
                dikt[r] = [False] * 10
            
            dikt[r][s-1] = True
        
        
        ans = 2 * n
        for r in dikt:
            count = 0
            temp = 0
            ans -= 2
            for s in range(1, 9):
                if dikt[r][s] == False:
                    count += 1
                else:
                    count = 0
                
                if count >= 4:
                    if s - 3 in [1,3,5]:
                        temp += 1
                        count = 0

            ans += temp
        return ans