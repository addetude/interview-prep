class Solution(object):
    def maxNumberOfBalloons(self, text):
        dic = {
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
        }
        for letter in text:
            if letter in "balon":
                dic[letter] += 1

        dic['l'] = dic['l'] // 2
        dic['o'] = dic['o'] // 2
        
        m = min(dic.values())

        return m

        