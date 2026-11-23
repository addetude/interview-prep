class Solution(object):
    def isValid(self, s):
        m = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        stack = []

        for b in s:
            if b in m:
                stack.append(b)
            else:
                if stack and m[stack[len(stack) - 1]] == b:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True