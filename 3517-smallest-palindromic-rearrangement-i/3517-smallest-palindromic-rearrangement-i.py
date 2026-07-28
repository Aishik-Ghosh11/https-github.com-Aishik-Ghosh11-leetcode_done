class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        frequency = [0 for _ in range(26)]
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        
        output = ['' for _ in range(n)]
        if n % 2 == 1:
            for i in range(26):
                if frequency[i] % 2 == 1:
                    output[n // 2] = chr(ord('a') + i)
                    frequency[i] -= 1
                    break
        
        pointer = 0
        for i in range(26):
            while frequency[i] > 0:
                output[pointer] = chr(ord('a') + i)
                output[n - pointer - 1] = chr(ord('a') + i)
                pointer += 1
                frequency[i] -= 2
        
        return ''.join(output)





























