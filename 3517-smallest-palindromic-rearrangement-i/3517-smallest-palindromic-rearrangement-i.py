class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = n//2

        s_list = list(s)
        s_list[:mid] = sorted(s_list[:mid])
        
        for i in range(mid):
            s_list[n - 1 - i] = s_list[i]
        
        return "".join(s_list)