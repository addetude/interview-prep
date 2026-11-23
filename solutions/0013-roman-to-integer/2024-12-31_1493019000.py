class Solution(object):
    def romanToInt(self, s):

        sum = 0
        for i in range(len(s)):
            if s[i] == "I":
                sum += 1
            elif s[i] == "V":
                sum += 5
                if i > 0:
                    if s[i-1] == "I":
                        sum -= 2
            elif s[i] == "X":
                sum += 10
                if i > 0:
                    if s[i-1] == "I":
                        sum -= 2
            elif s[i] == "L":
                sum += 50
                if i > 0:
                    if s[i-1] == "X":
                        sum -= 20
            elif s[i] == "C":
                sum += 100
                if i > 0:
                    if s[i-1] == "X":
                        sum -= 20
            elif s[i] == "D":
                sum += 500
                if i > 0:
                    if s[i-1] == "C":
                        sum -= 200
            elif s[i] == "M":
                sum += 1000  
                if i > 0:
                    if s[i-1] == "C":
                        sum -= 200

        return sum
        