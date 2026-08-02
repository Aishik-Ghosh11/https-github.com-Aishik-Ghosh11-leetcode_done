class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l , r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            pick_left = piles[l] - dfs(l+1 ,r)
            pick_right = piles[r] - dfs(l, r-1)

            dp[(l, r)] = max(pick_left , pick_right)
            return dp[(l, r)]

        return dfs(0, len(piles) - 1) > 0












