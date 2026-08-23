class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftKnownSum = 0
        rightKnownSum = 0
        leftQnMarkCount = 0
        rightQnMarkCount = 0

        for i in range(n):
            if num[i] == '?':
                if i < n / 2:
                    leftQnMarkCount += 1
                else:
                    rightQnMarkCount += 1
            else:
                if i < n / 2:
                    leftKnownSum += int(num[i])
                else:
                    rightKnownSum += int(num[i])

        totalQnMarkCount = leftQnMarkCount + rightQnMarkCount
        
        # If the total number of '?' is odd, Alice always wins
        if totalQnMarkCount % 2 == 1:
            return True

        LEFT = 2 * leftKnownSum + 9 * leftQnMarkCount
        RIGHT = 2 * rightKnownSum + 9 * rightQnMarkCount

        if LEFT == RIGHT:
            return False
        else:
            return True