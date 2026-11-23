class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map: tuple of letter frequency to list

        mapp = defaultdict(list)
        for word in strs:
            fq = [0] * 26

            for letter in word:
                index = ord(letter) - ord('a')
                fq[index] += 1
            
            mapp[tuple(fq)].append(word)

        return list(mapp.values())
