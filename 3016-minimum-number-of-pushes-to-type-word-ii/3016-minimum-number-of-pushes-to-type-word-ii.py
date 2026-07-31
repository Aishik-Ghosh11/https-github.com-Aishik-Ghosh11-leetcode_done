class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for i in range(len(word)):
            if word[i] in freq:
                freq[word[i]] += 1
            else:
                freq[word[i]] = 1
        freqs = sorted(freq.values(), reverse=True)
        summ = 0
        for i, f in enumerate(freqs):
            summ += f * (i //8 + 1)
        return summ