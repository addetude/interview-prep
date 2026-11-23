class Solution(object):
    def repeatedCharacter(self, s):
        sett = set()
        for char in s:
            if char in sett:
                return char
            else:
                sett.add(char)
        