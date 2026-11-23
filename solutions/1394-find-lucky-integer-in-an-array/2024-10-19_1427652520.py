class Solution(object):
    def findLucky(self, arr):
        arr_set = list(set(arr))
        max = -1
        length = len(arr_set)
        for i in range (length):
            f = arr.count(arr_set[i])
            if f == arr_set[i]:
                max = f
        return max
        
        