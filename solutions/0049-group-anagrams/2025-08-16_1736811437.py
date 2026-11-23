class Solution(object):
    def groupAnagrams(self, strs):
        
        dic = {}

        for s in strs:
            alpha = [0]*26
            for c in s:
                alpha[ord(c)-ord('a')] += 1
            alpha = tuple(alpha)
            if alpha in dic:
                dic[alpha].append(s)
            else:
                dic[alpha] = [s]

        res = []
        for key in dic:
            res.append(dic[key])
        
        return res


        

        