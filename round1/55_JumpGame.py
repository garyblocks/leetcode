class Solution(object):
    def canJump(self, nums):
        l = len(nums)
        cover = 0 
        for i in range(l):
            if i<=cover: 
                if i+nums[i]>=l-1:
                    return True
                elif i+nums[i]>cover:
                    cover=i+nums[i]
            else:
                return False
        """
        :type nums: List[int]
        :rtype: bool
        """