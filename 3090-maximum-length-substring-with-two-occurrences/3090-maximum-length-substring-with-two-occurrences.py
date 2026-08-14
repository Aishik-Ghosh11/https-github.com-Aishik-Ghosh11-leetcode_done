class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        else:
            new = 0
            for i in range(len(s)):
                subs = s[i:]
                for idx in range(len(subs)):
                    if subs[:idx].count(subs[idx]) == 2:
                        break
                    else:
                        longest = len(subs[:idx+1])
                        lon_str = subs[:idx+1]
                        print(idx, subs[:idx+1])
                if longest > new:
                    new = longest
            return new