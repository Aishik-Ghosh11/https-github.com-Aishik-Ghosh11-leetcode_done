class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        groups = []
        d = 0

        for c in seq:
            open = c == '('
            if open:
                d += 1
            groups.append(d % 2)
            if not open:
                d -= 1
        
        return groups

