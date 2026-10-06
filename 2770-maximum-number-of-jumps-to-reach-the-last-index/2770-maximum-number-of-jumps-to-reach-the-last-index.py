class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        d = defaultdict(int)

        if n == 1:
            return 0
        if n == 2:
            temp = nums[1] - nums[0]
            if temp >= -target and temp <= target:
                return 1
            return -1
        
        d[n-1] = 0

        for i in range(n-2 , -1, -1):
            m=0
            for j in range(i + 1, n):
                temp = nums[i] - nums[j]
                if (temp >= -target and temp <= target):
                    if d[j] == 0 and j < n-1:
                        m = max(m , 0)
                    else:
                        m = max(m, 1 + d[j])
            d[i] = m
            print(f"{i} \t\t {d[i]}")

        if not d[0]:
            return -1
        return d[0]

















