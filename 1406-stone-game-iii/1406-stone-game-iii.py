class Solution:
    def solve(self,index,dp,stone):
        l=len(stone)
        if index>=len(stone):
            return 0
        if dp[index]!=-1:
            return dp[index]

        #3cases to be considered
        #take 1 from left
        #take 2 from left
        #take 3 from left
        take1=take2=take3=float('-inf')
        take1=stone[index]+min(self.solve(index+2,dp,stone),self.solve(index+3,dp,stone),self.solve(index+4,dp,stone))
        if index+1<l:
            take2=stone[index]+stone[index+1]+min(self.solve(index+3,dp,stone),self.solve(index+4,dp,stone),self.solve(index+5,dp,stone))
        if index+2<l:
            take3=stone[index]+stone[index+1]+stone[index+2]+min(self.solve(index+4,dp,stone),self.solve(index+5,dp,stone),self.solve(index+6,dp,stone))
        dp[index]=max(take1,take2,take3)
        return dp[index]



    def stoneGameIII(self, stonevalue: List[int]) -> str:
        dp=[-1 for _ in range(len(stonevalue))]
        alice=self.solve(0,dp,stonevalue)
        bob=sum(stonevalue)-alice
        if alice>bob:
            return "Alice"
        elif alice==bob:
            return "Tie"
        return "Bob"
        