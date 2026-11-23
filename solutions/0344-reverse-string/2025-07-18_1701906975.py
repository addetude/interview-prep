class Solution(object):
    def reverseString(self, s):
        r = len(s) - 1
        l = 0
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        return s
        