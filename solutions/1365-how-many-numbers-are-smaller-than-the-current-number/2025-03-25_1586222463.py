class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        li = []
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] < num:
                    count += 1
            li.append(count)
        return li
            
        