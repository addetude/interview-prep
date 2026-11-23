class Solution(object):
    def defangIPaddr(self, address):
        string = ""
        length = len(address)
        for i in range(length):
            if address[i] == ".":
                string += "[.]"
            else:
                string += address[i]
        return string
        