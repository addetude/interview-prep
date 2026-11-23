class Solution(object):
    def shuffle(self, nums, n):
        arr_1 = []
        arr_2 = []
        arr = []
        for i in range(n):
            arr_1.append(nums[i])
            arr_2.append(nums[i + n])
            arr.append(arr_1[i])
            arr.append(arr_2[i])
        return arr
        