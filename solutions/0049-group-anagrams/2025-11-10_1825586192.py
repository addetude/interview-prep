class Solution(object):
    def groupAnagrams(self, strs):

        hmap = defaultdict(list)

        # loop through each str in strs
        for s in strs:
            d = self.makeDict(s)
            tup = tuple(d)
            if tup in hmap:
                hmap[tup].append(s)
            else:
                hmap[tup] = [s]

        res = []

        for key in hmap:
            res.append(hmap[key])

        return res

    def makeDict(self, s):
        arr = [0] * 26 
        for letter in s:
            i = ord(letter) - ord('a')
            arr[i] += 1
        return arr
        




        