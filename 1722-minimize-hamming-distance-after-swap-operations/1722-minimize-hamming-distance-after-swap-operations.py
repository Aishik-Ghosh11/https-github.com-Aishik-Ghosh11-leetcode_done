class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find_parent(i):
            while parent[i] != i:
                i = parent[i]
            return i
        
        for a, b in allowedSwaps:
            pa, pb = find_parent(a), find_parent(b)

            if pa == pb:
                continue
            elif pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb
        
        partition = defaultdict(set)
        for i in range(n):
            partition[find_parent(i)].add(i)
        
        res = 0
        for _, l in partition.items():
            c1 = Counter(source[idx] for idx in l)
            c2 = Counter(target[idx] for idx in l)
            for v, f in c2.items():
                res += max(0 , f - c1[v])
        
        return res

