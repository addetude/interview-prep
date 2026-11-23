class Solution(object):
    def isValid(self, s):
        stk = []
        h = {"{":"}", "[":"]", "(":")"}
        for bracket in s:
            if bracket in h:
                stk.append(bracket)
            else:
                if stk == []:
                    return False
                else:
                    if h[stk[-1]] == bracket:
                        stk.pop()
                    else:
                        return False
        if stk == []:
            return True
        else:
            return False

        