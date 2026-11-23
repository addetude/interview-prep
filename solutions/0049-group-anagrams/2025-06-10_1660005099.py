class Solution(object):
    def groupAnagrams(self, strs):
        bigD = defaultdict(list)
        for word in strs:
            letters = [0] * 26

            for c in word:
                letters[ord(c) - ord("a")] += 1
            
            bigD[tuple(letters)].append(word)

        return bigD.values()
        