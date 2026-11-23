class Solution(object):
    def isAnagram(self, s, t):
        S = {}
        T = {}
        
        for char in s:
            if char in S:
                S[char] += 1
            else:
                S[char] = 1
        
        for char in t:
            if char in T:
                T[char] += 1
            else:
                T[char] = 1

        if S == T:
            return True
        return False