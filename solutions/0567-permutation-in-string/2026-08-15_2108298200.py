class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        # create angaram for s1
        fixed = [0]*26
        working = [0]*26
        for letter in s1:
            index = ord(letter) - ord('a')
            fixed[index] += 1
        
        # iterate through s2 for permutation
        # set up initial window
        for i in range(0, n):
            index = ord(s2[i]) - ord('a')
            working[index] += 1

        print(working)
        print(fixed)
        
        r = n - 1
        l = 0
        while r < m - 1:
            if working == fixed:
                return True
            
            working[ord(s2[l]) - ord('a')] -= 1
            working[ord(s2[r + 1]) - ord('a')] += 1

            r += 1
            l += 1

        return working == fixed

