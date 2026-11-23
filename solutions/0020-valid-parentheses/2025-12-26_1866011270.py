class Solution(object):
    def isValid(self, s):
        stack = []
        bracket = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for c in s:
            if c in bracket:
                stack.append(c)
            else:
                if not stack or bracket.get(stack[-1]) != c:
                    return False
                stack.pop()
        
        if not stack:
            return True
        return False
        