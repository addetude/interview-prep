class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            "[":"]",
            "{":"}",
            "(":")",
        }
        for bracket in s:
            if bracket in "{([":
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if not pairs[top] == bracket:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        