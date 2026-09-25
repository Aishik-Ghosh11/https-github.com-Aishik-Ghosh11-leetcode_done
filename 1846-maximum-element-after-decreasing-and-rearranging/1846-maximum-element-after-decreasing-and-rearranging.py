class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)
        for i in range(n):
            arr[i] = min(arr[i], n)
        arr.sort()
        arr[0] = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        
        return arr[-1]

