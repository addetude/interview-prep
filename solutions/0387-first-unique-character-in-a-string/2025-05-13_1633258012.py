class Solution(object):
    def firstUniqChar(self, s):
        hmap = {}

        for letter in s:
            if not letter in hmap:
                hmap[letter] = 1
            else:
                hmap[letter] += 1
        
        for i in range(len(s)):
            if hmap.get(s[i], 0) == 1:
                return i
        
        return -1

