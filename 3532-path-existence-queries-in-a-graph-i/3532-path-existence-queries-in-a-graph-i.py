class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        num_to_min = {}
        section = nums[0]
        for i in range(0, len(nums)):
            if i > 0 and nums[i] > nums[i-1] + maxDiff:
                section = nums[i]
            num_to_min[nums[i]] = section
        print(num_to_min)
        res = []
        for query in queries:
            num0, num1 = nums[query[0]], nums[query[1]]
            print(num0, num1, num_to_min[num0], num_to_min[num1])
            if num_to_min[num0] == num_to_min[num1]:
                res.append(True)
            else:
                res.append(False)
        
        return res