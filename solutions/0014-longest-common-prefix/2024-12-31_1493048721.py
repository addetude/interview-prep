class Solution(object):
    def longestCommonPrefix(self, strs):
        m = min(strs)
        innit = True
        pf = ""
        for i in range(len(m)):
            letter = m[i]
            for word in strs:
                if word[i] != letter:
                    innit = False
            if innit == False:
                return pf
            else:
                pf += letter
        return pf
