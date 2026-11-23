class Solution(object):
    def longestConsecutive(self, nums):
        global_max = 0
        curr_max = 0
        s = set()

        for val in nums:
            s.add(val)

        for val in s:
            # start of sequence
            if val-1 not in s:
                global_max = max(global_max, curr_max)
                curr_max = 1
                num = val

                while num+1 in s:
                    curr_max += 1
                    num += 1

        global_max = max(global_max, curr_max)
        return global_max
        

        