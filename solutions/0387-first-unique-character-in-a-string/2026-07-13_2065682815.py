class Solution:
    def firstUniqChar(self, s: str) -> int:
        fq = [0]*26
        for letter in s:
            index = ord(letter) - ord('a')
            fq[index] += 1
        
        for i, letter in enumerate(s):
            index = ord(letter) - ord('a')
            if fq[index] == 1:
                return i
        
        return -1
