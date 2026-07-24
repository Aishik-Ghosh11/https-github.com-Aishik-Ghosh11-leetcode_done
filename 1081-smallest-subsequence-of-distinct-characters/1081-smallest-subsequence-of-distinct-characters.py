class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_pos = {ch: i for i, ch in enumerate(s)}
        stack = []
        in_stack = set()
        for i, ch in enumerate(s):
            if ch in in_stack:
                continue
            
            while stack and ch < stack[-1] and last_pos[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(ch)
            in_stack.add(ch)
        return ''.join(stack)