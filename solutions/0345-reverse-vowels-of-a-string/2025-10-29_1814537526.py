class Solution(object):
    def reverseVowels(self, s):
        
        l = 0
        r = len(s) - 1
        VOWELS = "aeiouAEIOU"
        li = list(s)

        while (l < r):
            while li[l] not in VOWELS and l < r:
                l += 1
            while li[r] not in VOWELS and l < r:
                r -= 1
            if (l < r):
                tmp = li[l]
                li[l] = li[r]
                li[r] = tmp
            l += 1
            r -= 1
        
        return "".join(li)
        


        