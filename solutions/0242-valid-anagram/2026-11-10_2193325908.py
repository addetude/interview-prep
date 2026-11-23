class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return self.createAnagram(s) == self.createAnagram(t)
    

    def createAnagram(self, s):
        m = {}
        for l in s:
            m[l] = m.get(l,0) + 1
        
        return m
        