class Solution(object):
    def calPoints(self, operations):
        stk = []

        for thing in operations:
            if thing == '+':
                stk.append(stk[-1] + stk[-2])
            elif thing == 'D':
                stk.append(stk[-1] * 2)
            elif thing == 'C':
                stk.pop()
            else:
                stk.append(int(thing))
        return sum(stk)


        