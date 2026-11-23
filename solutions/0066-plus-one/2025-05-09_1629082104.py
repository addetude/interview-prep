class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        num = 0
        for i in range(n):
            num += digits[i]*10**(n - i - 1)
        num += 1

        li = []
        while num > 0:
            li.insert(0, num % 10)
            num = num // 10
        
        return li


