class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        CHARS = 'abcdefghijklmnopqrstuvwxyz1234567890'

        while l <= r:
            if s[l].lower() not in CHARS:
                l += 1
            elif s[r].lower() not in CHARS:
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        
        return True
        
        