class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        fq = [0] * 26
        for letter in magazine:
            fq[ord(letter) - ord('a')] += 1
        
        for letter in ransomNote:
            fq[ord(letter) - ord('a')] -= 1
            if fq[ord(letter) - ord('a')] < 0:
                return False
        
        return True


        