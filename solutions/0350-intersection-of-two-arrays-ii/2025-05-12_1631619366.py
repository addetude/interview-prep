class Solution(object):
    def intersect(self, nums1, nums2):
        tab = {}
        arr = []

        for num in nums1:
            if num in tab:
                tab[num] += 1
            else:
                tab[num] = 1

        for num in nums2:
            if num in tab:
                if tab[num] == 0:
                    tab.pop(num)
                else:
                    tab[num] -= 1
                    arr.append(num)

        return arr

        