class Solution(object):
    def intersection(self, nums1, nums2):
        sett = set()
        arr = []

        for num in nums1:
            sett.add(num)
        
        nums2 = list(set(nums2))
        for num in nums2:
            if num in sett:
                arr.append(num)
        
        return arr
            
        
        return arr
        