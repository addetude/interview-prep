class Solution(object):
    def firstUniqChar(self, s):
        sett = set()
        arr = []

        for letter in s:
            if letter in sett:
                arr.append(letter)
            else:
                sett.add(letter)
        
        for i in range(len(s)):
            if s[i] not in arr:
                return i
        
        return -1

