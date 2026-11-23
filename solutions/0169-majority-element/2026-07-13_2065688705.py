class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fq = {}
        n = len(nums)
        for num in nums:
            fq[num] = fq.get(num, 0) + 1
            if fq[num] == n//2 + 1:
                return num

        return

