class Solution(object):
    def findWordsContaining(self, words, x):
        arr = []
        for i, word in enumerate(words):
            n = len(word)
            letter_in = 0
            while letter_in < n:
                if word[letter_in] == x:
                    arr.append(i)
                    break
                letter_in += 1
        return arr

        