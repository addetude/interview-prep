class Solution(object):
    def intersect(self, nums1, nums2):
        arr = []
        
        for num in nums2:
            if num in nums1:
                arr.append(num)
                nums1.remove(num)
        
        return arr

        