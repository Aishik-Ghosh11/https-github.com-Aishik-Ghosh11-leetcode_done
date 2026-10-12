class Solution:
    def mapWordWeights(self, words: List[str], wt: List[int]) -> str:
        res = []
        for word in words:
            word_weight = sum(wt[ord(char) - ord('a')] for char in word)
            letter = chr(ord('z') - word_weight % 26)
            res.append(letter)
        
        return "".join(res)