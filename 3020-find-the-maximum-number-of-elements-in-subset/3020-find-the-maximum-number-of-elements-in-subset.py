class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        max_cnt = 1
        cnt = Counter(nums)

        for num in nums:
            base = num
            if base == 1:
                max_cnt = max(cnt[base] - 1 + cnt[base]%2, max_cnt)
                continue
            k = 0
            while cnt[base] >= 2:
                base = base*base
                k += 1
            if cnt[base] == 1:
                k += 1
            max_cnt = max(2 * k-1, max_cnt)
        
        return max_cnt





