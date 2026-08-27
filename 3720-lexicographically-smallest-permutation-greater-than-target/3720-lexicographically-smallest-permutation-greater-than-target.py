from functools import cache
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        counts = [0]*26
        for i,c in enumerate(s):
            counts[ord(c)-ord('a')]+=1
        @cache
        def help(state, index):
            if index==len(target):
                return None
            tc = target[index]
            tc_ind = ord(tc)-ord('a')
            larger_char_ind = None
            for i in range(tc_ind+1, 26):
                if state[i] > 0:
                    larger_char_ind = i
                    break
            cand = None
            if larger_char_ind is not None:
                chrs = [chr(ord('a')+larger_char_ind)]
                for i,c in enumerate(state):
                    if i == larger_char_ind:
                        c -= 1
                    chrs.append(chr(ord('a')+i)*c)
                cand = ''.join(chrs)
            if state[tc_ind] > 0:
                cl = list(state)
                cl[tc_ind] -= 1
                next_state = tuple(cl)
                next_str = help(next_state, index+1)
                if next_str is not None:
                    if cand is None:
                        cand = tc + next_str
                    else:
                        cand = min(cand, tc+next_str)
            return cand
        ans= help(tuple(counts),0)
        return '' if ans is None else ans