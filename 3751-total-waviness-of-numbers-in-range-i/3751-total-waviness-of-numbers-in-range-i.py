class Solution:
    def totalWaviness(self, A: int, B: int) -> int:
        ans = 0

        for num in range(A, B+1):
            str_num = str(num)
            for index, ch in enumerate(str_num):
                if index == 0 or index == len(str_num) - 1:
                    continue
                if (int(ch) > int(str_num[index-1]) and int(ch) > int(str_num[index+1])):
                    ans += 1
                if (int(ch) < int(str_num[index-1]) and int(ch) < int(str_num[index+1])):
                    ans += 1
        
        return ans
        
                


