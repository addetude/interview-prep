class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0
        for char in s:
            if char == letter:
                count += 1
        
        return 100 * count // len(s)
        