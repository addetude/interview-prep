class Solution(object):
    def summaryRanges(self, nums):

        if not nums:
            return nums
        elif len(nums) == 1:
            return [str(nums[0])]

        d = []
        a = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if a != nums[i - 1]:
                    d.append(str(a)+"->"+str(nums[i - 1]))
                    a = nums[i]
                else: 
                    d.append(str(a))
                    a = nums[i]
            if i == len(nums) - 1:
                if a == nums[i]:
                    d.append(str(a))
                else:
                    d.append(str(a)+"->"+str(nums[i]))

        return d



        