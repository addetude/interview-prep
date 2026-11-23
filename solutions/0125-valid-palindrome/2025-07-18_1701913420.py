class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1

        ALPHA = 'abcdefghijklmnopqrstuvwxyz1234567890'
        
        while l < r:
            if not s[l].lower() in ALPHA:
                l += 1
            elif not s[r].lower() in ALPHA:
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
            
        return True