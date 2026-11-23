class Solution(object):
    def mergeAlternately(self, word1, word2):
        new = ""
        len1 = len(word1)
        len2 = len(word2)
        m = len1
        s = ""
        if len1 < len2:
            m = len1
            for i in range(len1, len2):
                s += word2[i]
        elif len2 < len1:
            m = len2
            for i in range(len2, len1):
                s += word1[i]
        for i in range(m):
            new += (word1[i])
            new += (word2[i])
        return new + s
        
        