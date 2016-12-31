class Solution(object):
    def removeDuplicates(self, nums):
        lo,hi = 0,0
        l = len(nums)
        if l==0 or l==1:
            return l
        while hi<l:
            while hi+1<l and nums[hi]==nums[hi+1]:
                hi+=1
            if lo>0 and nums[lo]<=nums[lo-1]:
                nums[lo],nums[hi]=nums[hi],nums[lo]
            hi+=1
            lo+=1
        return lo
                
        """
        :type nums: List[int]
        :rtype: int
        """