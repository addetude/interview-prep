class Solution(object):
    def countGoodSubstrings(self, s):
        n = len(s)
        count = 0

        for i in range(n - 2):
            sett = set()
            sett.add(s[i])
            sett.add(s[i + 1])
            sett.add(s[i + 2])
            if len(sett) == 3:
                count += 1
        
        return count
        