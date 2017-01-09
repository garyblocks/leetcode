class Solution(object):
    def sortColors(self, nums):
        lo,hi = 0,len(nums)-1
        i = lo
        while lo<=i<=hi:
            if nums[i] == 0:
                nums[i],nums[lo] = nums[lo],nums[i]
                lo+=1
                if i<lo:
                    i=lo
            elif nums[i] == 2:
                nums[i],nums[hi] = nums[hi],nums[i]
                hi-=1
            else:
                i+=1
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """