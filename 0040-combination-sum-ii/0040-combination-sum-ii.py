class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        curr = []

        def func(i,total):
            nonlocal res,curr
            if total == target:
                res.append(curr[:])
                return
            
            if i == len(candidates) or total > target:
                return
            
            total += candidates[i]
            curr.append(candidates[i])
            func(i+1,total)
            total -= candidates[i]
            curr.pop()

            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            func(i+1,total)
        
        func(0,0)
        return res