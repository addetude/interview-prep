class Solution(object):
    def isAnagram(self, s, t):
        S = len(s)
        T = len(t)
        d = {}

        if S != T:
            return False

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for char in t:
            if char in d:
                d[char] -= 1
                if d[char] < 0:
                    return False
            else:
                return False
        
        if max(d.values()) == 0 and min(d.values()) == 0:
            return True
        else:
            return False

