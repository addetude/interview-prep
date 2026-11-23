class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sett = set()
        l = r = currMax = maxx = 0

        while r < len(s):
            if s[r] in sett:
                if currMax > maxx:
                    maxx = currMax
                currMax -= 1
                sett.remove(s[l])
                l += 1
                
            else:
                sett.add(s[r])
                currMax += 1
                r += 1

        if currMax > maxx:
            maxx = currMax

        return maxx



        
        