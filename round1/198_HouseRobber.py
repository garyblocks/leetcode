class Solution(object):
    def rob(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0],nums[1])
        else:
            mid = int(l/2)
            a = self.rob(nums[:mid])+self.rob(nums[mid+1:])
            b = nums[mid]+self.rob(nums[:mid-1])+self.rob(nums[mid+2:])
            return max(a,b)
        """
        :type nums: List[int]
        :rtype: int
        """