class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m>n: return -1
        for i in range(n-m+1):
            flag=True
            for j in range(m):
                if haystack[i+j]!=needle[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1