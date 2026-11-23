class Solution(object):
    def firstUniqChar(self, s):
        ddict = defaultdict(int)

        for char in s:
            ddict[char] += 1
        
        for i, char in enumerate(s):
            if ddict[char] == 1:
                return i
        
        return -1



