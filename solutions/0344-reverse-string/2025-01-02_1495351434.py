class Solution(object):
    def reverseString(self, s):
        o = len(s) - 1
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[o - i]
            s[o - i] = temp
        return s
        