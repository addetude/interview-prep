class Solution(object):
    def reverseString(self, s):
        r = len(s) - 1
        l = 0
        while r > l:
            s[r], s[l] = s[l], s[r]
            r -= 1
            l += 1 
        return s
        