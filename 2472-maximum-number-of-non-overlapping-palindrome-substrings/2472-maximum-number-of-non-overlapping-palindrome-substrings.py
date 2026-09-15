class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        palindromeDp = [[False for _ in range(n)] for j in range(n)]

        for i in range(n):
            palindromeDp[i][i] = True
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        palindromeDp[i][j] = True
                    else:
                        palindromeDp[i][j] = palindromeDp[i+1][j-1]

        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):

            dp[i] = dp[i+1]
            for j in range(i + k - 1, n):
                if palindromeDp[i][j]:
                    dp[i] = max(dp[i], 1 + dp[j+1])
        
        return dp[0]








