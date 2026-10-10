class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        budget = k1 + k2

        if sum(diffs) <= budget:
            return 0
        
        groups = sorted(Counter(diffs).items(), reverse = True)
        groups.append((0, 0))

        group_count = 0

        for g in range(len(groups) - 1):
            height, count = groups[g]
            next_height = groups[g + 1][0]

            group_count += count
            gap = height - next_height
            cost_to_absorb = gap * group_count

            if budget >= cost_to_absorb:
                budget -= cost_to_absorb
            
            else:
                full_drop = budget // group_count
                extra_drop_count = budget % group_count
                new_level = height - full_drop

                result = (
                    (group_count - extra_drop_count) * new_level ** 2
                    + extra_drop_count * (new_level - 1) ** 2
                )

                for h, c in groups[g + 1:-1]:
                    result += c * h * h
                return result
            
        return 0






























