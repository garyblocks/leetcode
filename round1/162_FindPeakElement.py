class Solution(object):
    def findPeakElement(self, nums):
        prev = -2147483649
        flag = False
        for i in range(len(nums)):
            if nums[i]>prev:
                flag = True
            elif flag:
                return i-1
            else:
                flag = False
            prev = nums[i]
        if len(nums)>1 and nums[-2]<nums[-1]:
            return len(nums)-1
        elif len(nums)==1:
            return 0
        """
        :type nums: List[int]
        :rtype: int
        """