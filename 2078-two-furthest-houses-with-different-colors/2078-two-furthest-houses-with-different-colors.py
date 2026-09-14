class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d=1
        k=1
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    k=abs(i-j)
                d=max(k,d)
        return d