class Solution(object):
    def isAnagram(self, s, t):
        return self.toAlpha(s) == self.toAlpha(t)
        
    def toAlpha(self, s):
        alpha = [0] * 26
        for letter in s:
            alpha[ord(letter) - ord('a')] += 1
        return alpha