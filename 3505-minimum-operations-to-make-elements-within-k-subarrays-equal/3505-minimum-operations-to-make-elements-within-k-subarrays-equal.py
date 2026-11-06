import numpy as np

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        if n < x * k:
            return -1
            
        small = []   # Max-heap (negated)
        large = []   # Min-heap
        delayed = defaultdict(int)
        
        sSize = 0
        lSize = 0
        sSum = 0
        lSum = 0
        
        # 1. Fixed list multiplication syntax
        cost = [0] * (n - x + 1)

        # Cache built-in methods to local variables to eliminate attribute lookup overhead
        push = heappush
        pop = heappop

        # 2. Sliding Window Stage
        for i in range(n):
            v = nums[i]
            
            # Fixed heap top index syntax from small to small[0]
            if not small or v <= -small[0]:
                push(small, -v)
                sSize += 1
                sSum += v
            else:
                push(large, v)
                lSize += 1
                lSum += v
            
            # Inlined balancing code with integrated prunes to save function call overhead
            while sSize > lSize + 1:
                top_v = -pop(small)
                sSize -= 1
                sSum -= top_v
                push(large, top_v)
                lSize += 1
                lSum += top_v
                while small and delayed[-small[0]] > 0:
                    delayed[-small[0]] -= 1
                    pop(small)
                    
            while sSize < lSize:
                top_v = pop(large)
                lSize -= 1
                lSum -= top_v
                push(small, -top_v)
                sSize += 1
                sSum += top_v
                while large and delayed[large[0]] > 0:
                    delayed[large[0]] -= 1
                    pop(large)
            
            if i >= x:
                out = nums[i - x]
                delayed[out] += 1
                if out <= -small[0]:
                    sSize -= 1
                    sSum -= out
                    if out == -small[0]:
                        while small and delayed[-small[0]] > 0:
                            delayed[-small[0]] -= 1
                            pop(small)
                else:
                    lSize -= 1
                    lSum -= out
                    if large and out == large[0]:
                        while large and delayed[large[0]] > 0:
                            delayed[large[0]] -= 1
                            pop(large)
                            
                while sSize > lSize + 1:
                    top_v = -pop(small)
                    sSize -= 1
                    sSum -= top_v
                    push(large, top_v)
                    lSize += 1
                    lSum += top_v
                    while small and delayed[-small[0]] > 0:
                        delayed[-small[0]] -= 1
                        pop(small)
                        
                while sSize < lSize:
                    top_v = pop(large)
                    lSize -= 1
                    lSum -= top_v
                    push(small, -top_v)
                    sSize += 1
                    sSum += top_v
                    while large and delayed[large[0]] > 0:
                        delayed[large[0]] -= 1
                        pop(large)
                
            if i >= x - 1:
                med = -small[0]
                cost[i - x + 1] = med * (sSize - lSize) - sSum + lSum

        INF = 1 << 60
        m = n - x + 1
        cost_np = np.array(cost, dtype=np.int64)
        dp_prev = np.zeros(n + 1, dtype=np.int64)
        b = np.empty(n + 1, dtype=np.int64)
        
        for _ in range(k):
            b[:] = INF
            b[x:] = dp_prev[0:m] + cost_np
            dp_prev = np.minimum.accumulate(b)
            
        return int(dp_prev[-1])