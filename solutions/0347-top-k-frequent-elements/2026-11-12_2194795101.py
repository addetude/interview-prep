class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        m = {}
        length = len(nums)
        for n in nums:
            m[n] = m.get(n,0) + 1
        
        alph = [[] for _ in range(length + 1)]

        for key in m:
            alph[m[key]].append(key)

        res = []
        l = len(alph) - 1

        while len(res) < k:
            res.extend(alph[l])
            l -= 1
        
        return res










