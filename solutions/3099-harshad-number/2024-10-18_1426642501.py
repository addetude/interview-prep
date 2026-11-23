class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        x = str(x)
        num = 0
        for i in range(len(x)):
            num += int(x[i])

        if int(x) % num == 0:
            return num
        else:
            return -1
        