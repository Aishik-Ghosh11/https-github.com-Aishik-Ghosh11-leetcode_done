class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        v=[nums[0]]
        o=[]
        h=[]
        w=0
        for i in range(1,len(nums)):
            c=max(nums[0:i])
            v.append(c)
            p=min(nums[w:])
            w+=1
            o.append(p)
        o.append(nums[len(nums)-1])    
        for i in range(0,len(nums)):
            c=v[i]-o[i]
            h.append(c)
        for i in range(0,len(nums)):  
            if h[i] <= k:
                return i
        return -1
       
       

        