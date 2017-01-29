class Solution(object):
    def findMin(self, nums):
        min = nums[0]
        for i in nums:
            if i<min:
                min = i
        return min
        """
        :type nums: List[int]
        :rtype: int
        """