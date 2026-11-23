class Solution(object):
    def isPalindrome(self, s):
        ALPHA = "abcdefghijklmnopqrstuvwxyz0123456789"
        l = 0
        r = len(s) - 1

        while l < r:
            while s[l].lower() not in ALPHA and l < r:
                l += 1
            while s[r].lower() not in ALPHA and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
        
        
        