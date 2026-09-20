class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        left = [n] * 26
        right = [-1] * 26
        
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = max(right[idx], i)
            
        intervals = []
        for i in range(26):
            if left[i] == n:
                continue
            
            l, r = left[i], right[i]
            valid = True
            j = l
            while j <= r:
                char_idx = ord(s[j]) - ord('a')
                
                if left[char_idx] < l:
                    valid = False
                    break
        
                r = max(r, right[char_idx])
                j += 1
            if valid:
                intervals.append([l, r])
                
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l:r+1])
                prev_end = r
                
        return res