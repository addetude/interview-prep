class Solution(object):
    def topKFrequent(self, nums, k):
        track = {}
        arr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            track[num] = track.get(num, 0) + 1

        for c, v in track.items():
            arr[v].append(c)
        
        res = []
        
        for i in range(len(arr) - 1, -1, -1 ):
            for j in range(len(arr[i])):
                if len(res) < k:
                    res.append(arr[i][j])
                else:
                    return res

        return res

        