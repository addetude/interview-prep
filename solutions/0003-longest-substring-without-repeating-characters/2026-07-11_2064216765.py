class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        sett = set()
        first = 0
        last = 0
        longest = 1
        sett.add(s[first])

        while last < n-1:
            last += 1
            if s[last] in sett:
                while s[first] != s[last]:
                    sett.remove(s[first])
                    first += 1
                first += 1
            else:
                sett.add(s[last])
                if last - first + 1 > longest:
                    longest = last - first + 1
        
        return longest



