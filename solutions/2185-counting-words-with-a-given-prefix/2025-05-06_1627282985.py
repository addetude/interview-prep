class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        n = len(pref)

        for word in words:
            if word[:n] == pref:
                count += 1
        
        return count
        