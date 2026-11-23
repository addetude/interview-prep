class Solution(object):
    def groupAnagrams(self, strs):

        hmap = defaultdict(list)

        for s in strs:
            arr = [0] * 26 

            for c in s:
                i = ord(c) - ord('a')
                arr[i] += 1
        
            tup = tuple(arr)
            hmap[tup].append(s)

        return hmap.values()




        