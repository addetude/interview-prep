class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0 
       
        sett = set()
        l = 0
        r = 0
        m = 0

        while r < n:
            if s[r] in sett:
                while s[l] != s[r]:
                    sett.remove(s[l])
                    l += 1
                l += 1
            else:
                sett.add(s[r])

            m = max(m, r - l + 1)
            r += 1
        
        return m