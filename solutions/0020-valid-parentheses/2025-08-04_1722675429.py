class Solution(object):
    def isValid(self, s):
        ref = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []

        for char in s:
            if char in ref:
                stack.append(char)
            else:
                if not stack or ref[stack[-1]] != char:
                    return False
                stack.pop()
        
        if not stack:
            return True
        return False
        