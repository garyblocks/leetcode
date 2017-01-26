class Solution(object):
    def findMin(self, nums):
        def find(nums,start,end):
            mid = (start+end)/2
            if mid+1<sz:
                if nums[mid+1]<nums[mid]:
                    return nums[mid+1]
                elif nums[mid]>nums[-1]:
                    return find(nums,mid,end)
                else:
                    return find(nums,start,mid)
            else:
                return nums[mid]
        sz = len(nums)
        if nums[-1]>nums[0]:
            return nums[0]
        return find(nums,0,sz-1)
        """
        :type nums: List[int]
        :rtype: int
        """