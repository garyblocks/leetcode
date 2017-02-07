class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        delta = 0
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i+1]-nums[i]>delta:
                delta = nums[i+1]-nums[i]
        return delta
        """
        :type nums: List[int]
        :rtype: int
        """