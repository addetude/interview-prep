class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                if abs(h[nums[i]] - i) <= k:
                    return True
                else:
                    h[nums[i]] = i
            else:
                h[nums[i]] = i
        return False