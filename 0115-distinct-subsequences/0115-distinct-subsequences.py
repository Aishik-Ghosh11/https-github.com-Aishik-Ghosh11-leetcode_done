class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        f = cache(lambda i,j:j==-1 if -1 in (i,j) else f(i-1,j)+(s[i]==t[j])*f(i-1,j-1))
        return f(len(s)-1,len(t)-1)   