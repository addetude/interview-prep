class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_len = 0
        sett = set()

        l = 0
        r = 0

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
