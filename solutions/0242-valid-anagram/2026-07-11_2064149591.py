class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        fq = [0]*26

        for letter in s:
            index = ord(letter) - ord('a')
            fq[index] += 1

        for letter in t:
            index = ord(letter) - ord('a')
            fq[index] -= 1 

            if fq[index] < 0:
                return False
            
        if fq == [0]*26:
            return  True

        return False 


        