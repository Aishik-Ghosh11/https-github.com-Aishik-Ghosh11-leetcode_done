class Solution:
    def minOperations(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        ans1 = 0
        t = s[0]
        for i in range(1, len(s)):
            if s[i] == t:
                ans1 += 1
                t = str(1 - int(s[i]))
            else:
                t = s[i]
        ans2 = 1
        t = str(1 - int(s[0]))
        for i in range(1, len(s)):
            if s[i] == t:
                ans2 += 1
                t = str(1 - int(s[i]))
            else:                
                t = s[i]
        return min(ans1, ans2)
            