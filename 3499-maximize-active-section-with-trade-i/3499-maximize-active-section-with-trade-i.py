class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if not s or '1' not in s: return 0
        if len(s) == 1: return 1 if s == '1' else 0
        s = s + '1'
        cur = '1'
        arr = [1]
        for x in s:
            if x == cur == '1':
                arr[-1]+=1
            elif x == cur == '0':
                arr[-1]+=1 #arr[-1]-=1
            elif x == '0':
                arr.append(1)
                cur = x
            else:
                arr.append(1)
                cur=x
        if len(arr) < 5: return s[:-1].count('1')
        l, r = 0, 4
        arr[0]-=1; arr[-1]-=1
        cur_max=total_sum=sum(arr[::2]); best_r = 1, 3
        # print(arr)
        while r < len(arr):
            # temp_sum = total_sum-sum(arr[l:r+1])+ 2*(arr[l+1] + arr[r-1])
            temp_sum = total_sum + (arr[l+1] + arr[r-1])
            if temp_sum >= cur_max:
                cur_max = temp_sum
                best_l, best_r = l + 1, r - 1
            l+=2
            r+=2
        # for i in range(len(arr)):
        # print(f"cur_max: {cur_max}, best_l: {best_l}, best_r: {best_r}")
        return total_sum + arr[best_l] + arr[best_r]