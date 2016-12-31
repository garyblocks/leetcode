class Solution(object):
    def removeElement(self, nums, val):
        lo,hi = 0,len(nums)-1
        while lo<=hi:
            if nums[lo]==val:
                while hi>=0 and nums[hi]==val:
                    hi-=1
                if hi>lo:
                    nums[lo],nums[hi]=nums[hi],nums[lo]
                else:
                    break
            else:
                lo+=1
        return lo
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """