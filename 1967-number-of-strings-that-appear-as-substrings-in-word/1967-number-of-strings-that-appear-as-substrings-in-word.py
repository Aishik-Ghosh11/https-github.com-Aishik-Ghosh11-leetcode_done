class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        cnt = 0
        for s in patterns:
            if word.find(s) != -1:
                cnt += 1
        return cnt