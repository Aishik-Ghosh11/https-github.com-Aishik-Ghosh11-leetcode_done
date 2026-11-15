class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans=[[0]* n for _ in range(n)]
        top,bottom,left,right=0,n-1,0,n-1
        ele=1
        while top<=bottom and left<=right:
            for _ in range(left,right+1):
                ans[top][_]=ele
                ele+=1
            top+=1
            for _ in range(top,bottom+1):
                ans[_][right]=ele
                ele+=1
            right-=1
            if top<=bottom:
                for _ in range(right,left-1,-1):
                    ans[bottom][_]=ele
                    ele+=1
                bottom-=1
            if left<=right:
                for _ in range(bottom,top-1,-1):
                    ans[_][left]=ele
                    ele+=1
                left+=1
        return ans