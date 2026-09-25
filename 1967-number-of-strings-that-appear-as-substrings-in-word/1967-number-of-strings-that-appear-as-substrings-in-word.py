class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        def is_substring(pattern, word):
            n = len(pattern)
            m = len(word)

            for j in range(m):
                i=0
                while i < n and j < m and pattern[i] == word[j]:
                    j += 1
                    i += 1
                
                if i == n:
                    return True
            return False
        
        res = 0
        for pattern in patterns:
            if is_substring(pattern, word):
                res += 1

        return res
