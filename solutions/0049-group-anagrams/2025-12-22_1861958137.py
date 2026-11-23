class Solution(object):
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            tupS = self.toTuple(s)
            d[tupS].append(s)
        return d.values()

    def toTuple(self, s):
        l = [0] * 26
        for letter in s:
            l[ord(letter) - ord('a')] += 1
        return tuple(l)

        