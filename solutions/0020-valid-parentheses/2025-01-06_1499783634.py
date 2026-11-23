class Solution(object):
    def isValid(self, s):
        stk = []
        for bracket in s:
            if bracket in "{[(":
                stk.append(bracket)
            else: # closing bracket
                if stk == []:
                    return False
                else: 
                    brac = stk[-1]
                if bracket == ")":
                    if brac == "(":
                        stk.pop()
                    else:
                        return False
                elif bracket == "}":
                    if brac == "{":
                        stk.pop()
                    else:
                        return False
                else: # is ]
                    if brac == "[":
                        stk.pop()
                    else:
                        return False
        if not stk:
            return True
        else:
            return False


        