class Solution(object):
    def groupAnagrams(self, strs):
        m = defaultdict(list)
        for s in strs:
            tup = self.createAnagram(s)
            if tup in m:
                m[tup].append(s)
            else:
                m[tup] = [s]
        
        return m.values()
        



    def createAnagram(self, s):

        # should return tuple frequency map
        alpha = [0]*26

        for l in s:
            alpha[ord(l)-ord('a')] += 1

        return tuple(alpha)

        