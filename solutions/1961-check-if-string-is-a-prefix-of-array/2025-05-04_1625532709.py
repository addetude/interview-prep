class Solution(object):
    def isPrefixString(self, s, words):

        for i in range(len(words)):
            if words[i] != s[0:len(words[i])]:
                return False
            s = s[len(words[i]):]
            if s == "":
                return True

        if len(s) != 0:
            return False
        return True
        