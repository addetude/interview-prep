class Solution(object):
    def isSubsequence(self, s, t):
        count = 0
        j = 0
        while j < len(s) and count < len(t):
            letter = s[j]
            if letter == t[count]:
                j += 1
            count += 1
        if j == len(s):
            return True
        else:
            return False
        