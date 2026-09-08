class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        hm = {}
        for num, indices in pos.items():
            m = len(indices)
            if m == 1:
                hm[indices[0]] = -1
            else:
                for i in range(m):
                    curr = indices[i]
                    left = indices[i-1]
                    right = indices[(i + 1) % m]

                    dist_left = min(abs(curr - left) , n - abs(curr - left))
                    dist_right = min(abs(curr - right), n - abs(curr - right))

                    hm[curr] = min(dist_left , dist_right)
        answer = []
        for q in queries:
            answer.append(hm[q])
            
        return answer







