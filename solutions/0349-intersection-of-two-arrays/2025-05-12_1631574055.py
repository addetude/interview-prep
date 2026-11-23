class Solution(object):
    def intersection(self, nums1, nums2):
        arr = []

        nums1 = set(nums1)
        nums2 = list(set(nums2))
        for num in nums2:
            if num in nums1:
                arr.append(num)
            
        return arr
        