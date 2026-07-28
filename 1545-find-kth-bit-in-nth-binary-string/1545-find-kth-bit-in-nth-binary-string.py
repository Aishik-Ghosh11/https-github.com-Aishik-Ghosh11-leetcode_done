class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        l=[]
        for x in range(n):
            l+=[s]
            t=["1" if x=="0" else "0" for x in s]
            s=s+"1"+"".join(t[::-1])
        return l[-1][k-1]
