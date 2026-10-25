class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        sum_num_arr = []

        for number in nums:
            str_num = str(number)
            total_sum = sum(int(digit) for digit in str_num)
            sum_num_arr.append(total_sum)

        return min(sum_num_arr)