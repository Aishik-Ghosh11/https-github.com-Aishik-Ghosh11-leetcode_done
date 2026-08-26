class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        prefix = [0]*(n+1)
        for i in range(1,n+1):
            if s[i-1] == '1':
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
        
        res = ""
        for j in range(1, n+1):
            for i in range(j):
                if prefix[j]-prefix[i] == k:
                    if (not res) or j-i < len(res):
                        res = s[i:j]
                    elif j-i == len(res) and s[i:j] < res:
                        res = s[i:j]
        return res
