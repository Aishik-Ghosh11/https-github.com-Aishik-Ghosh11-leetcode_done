class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        arr=[]
        for i in range(0,len(nums)):
            if(nums[i])<pivot:
                arr.append(nums[i])
        for i in range(0,len(nums)):
            if(nums[i])==pivot:
                arr.append(nums[i])
        for i in range(0,len(nums)):
            if(nums[i])>pivot:
                arr.append(nums[i])
        nums=arr
        print(nums)
        return nums