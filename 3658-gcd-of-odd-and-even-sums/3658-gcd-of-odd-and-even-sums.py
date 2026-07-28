class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        num = 1
        count = 0
        while count < n+n:
            if num % 2 == 0:
                sumEven += num
            if num % 2 == 1:
                sumOdd += num
            count += 1
            num += 1
        while sumEven != 0:
            sumOdd, sumEven = sumEven, sumOdd % sumEven
        return sumOdd

