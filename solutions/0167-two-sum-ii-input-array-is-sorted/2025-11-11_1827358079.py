class Solution(object):
    def twoSum(self, numbers, target):
        # One pointer on l and one on r
        l = 0
        r = len(numbers) - 1

        # if target is > current sum, r -= 1 and l += is <
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        return []      