class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapp = {}
        for letter in s:
            mapp[letter] = mapp.get(letter, 0) + 1

        for i, letter in enumerate(s):
            if mapp[letter] == 1:
                return i
        
        return -1

        