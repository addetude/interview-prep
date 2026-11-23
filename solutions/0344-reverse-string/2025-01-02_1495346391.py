class Solution(object):
    def reverseString(self, s):
        r = len(s) - 1
        l = 0
        while r > l:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            r -= 1
            l += 1 
        return s
        