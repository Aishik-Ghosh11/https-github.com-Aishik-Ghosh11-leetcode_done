class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = [[nums[i], i] for i in range(n)]
        arr.sort(key=lambda x:x[0])

        uf = UnionFind(n)
        for i in range(n-1):
            if arr[i+1][0] - arr[i][0] <= limit :
                uf.union(arr[i+1][1], arr[i][1])
        
        myMap = defaultdict(list)
        myMapIndex = defaultdict(list)

        for i in range(n):
            key = uf.find(i)
            myMap[key].append(nums[i])
            myMapIndex[key].append(i)
        
        for key in myMap:
            myMap[key].sort()
        
        ans = [0] * n

        for key in myMap:
            for i in range(len(myMap[key])):
                ans[myMapIndex[key][i]] = myMap[key][i]
            
        return ans



class UnionFind:

    def __init__(self, n: int):
        self.n = n
        self.root = [0]*n
        for i in range(n):
            self.root[i] = i


    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        else:
            return self.find(self.root[x])

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootX] = rootY

    