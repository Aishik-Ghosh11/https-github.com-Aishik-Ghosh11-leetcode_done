class Solution:
    def evaluate(self, s: str, K: list[list[str]]) -> str:
        """
        handling empty strings...

        """
        k_map = {}
        for k, v in K:
            k_map[k] = v

        to_clear = []

        i=0
        while i < len(s):

            while i < len(s) and s[i] != '(':
                i += 1
            start = i

            while i < len(s) and s[i] != ')':
                i += 1
            
            end = i

            word = s[start+1: end]
            if start != end:
                to_clear.append((start, end, word))
            
            i += 1
        
        s = list(s)
        while to_clear:
            start , end, word = to_clear.pop()
            s[start:end + 1] = list(k_map.get(word, '?'))
        
        return "".join(s)









