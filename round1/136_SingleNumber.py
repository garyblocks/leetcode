class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        sum = 0
        sign = -1
        for i in nums:
            sign *= -1
            sum += sign*i
        return sum
        """
        :type nums: List[int]
        :rtype: int
        """