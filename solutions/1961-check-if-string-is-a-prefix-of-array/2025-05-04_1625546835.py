class Solution(object):
    def isPrefixString(self, s, words):

        c = ""
        
        for word in words:
            c += word
            if not s.startswith(c):
                return False
            if c == s:
                return True
        
        return False
        