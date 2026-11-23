class Solution(object):
    def getSneakyNumbers(self, nums):
        sett = set()
        res = []
        for num in nums:
            if num in sett:
                res.append(num)
            else:
                sett.add(num)
        return res

        