class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count_zero=0
        zero_idx=len(nums)
        for idx,n in enumerate(nums):
            if n==0: 
                count_zero+=1
                zero_idx=idx
        if (count_zero==0) or (count_zero==1 and zero_idx==len(nums)-1):
            return True
        cur_start_success=dict()
        def can_reach_to_end(cur_start):
            #print(f"cur_start={cur_start}")
            if cur_start in cur_start_success:
                #print(f"cur_start={cur_start}, cur_start_success[cur_start]={cur_start_success[cur_start]}")
                return cur_start_success[cur_start]
            if cur_start>=len(nums)-1:
                return True
            # if nums[cur_start]==0: 
            #     return False
            for s in range(nums[cur_start], 0, -1):
                #print(f"cur_start={cur_start}, s={s}")
                if cur_start+s<len(nums) and cur_start+s not in cur_start_success:
                    re=can_reach_to_end(cur_start+s)
                    if re:
                        cur_start_success[cur_start]=True
                        return True
            cur_start_success[cur_start]=False
            return False
        
        return can_reach_to_end(0)

            
        