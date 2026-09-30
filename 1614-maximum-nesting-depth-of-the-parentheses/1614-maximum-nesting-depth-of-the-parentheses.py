class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        curr_depth = 0
        for c in s:
            if c == '(':
                curr_depth += 1
                ans = max(ans , curr_depth)
            if c == ')':
                curr_depth -= 1
        
        return ans























            