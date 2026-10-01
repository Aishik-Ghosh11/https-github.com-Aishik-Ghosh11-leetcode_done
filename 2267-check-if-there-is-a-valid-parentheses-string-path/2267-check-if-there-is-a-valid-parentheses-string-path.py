class Solution:
    def hasValidPath(self, g: List[List[str]]) -> bool:
        return(f:=cache(lambda x,y,k,m=len(g),n=len(g[0]):x<m*(y<n)and(v:=k+(g[x][y]<')')*2-1)>0 and(f(x+1,y,v)|f(x,y+1,v)or x+y+4>m+n+v)))(0,0,1)