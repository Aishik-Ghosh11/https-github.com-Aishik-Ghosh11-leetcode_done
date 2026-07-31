class Solution:
    def minOperations(self, s: str) -> int:
        st0, st1 = 0,0
        for i in range(len(s)):
            st0 += (s[i] == str(i % 2))
            st1 += (s[i] == str((i + 1) % 2))
        return min(st0, st1)
