class Solution(object):
    def mergeAlternately(self, word1, word2):
        new = ""
        len1 = len(word1)
        len2 = len(word2)
        if len1 < len2:
            m = len1
            ma = len2
        else:
            m = len2
            ma = len1

        for i in range(ma):
            if i < m:
                new += (word1[i])
                new += (word2[i])
            else:
                if len1 < len2:
                    new += word2[i]
                elif len2 < len1:
                    new += word1[i]
        return new
        
        