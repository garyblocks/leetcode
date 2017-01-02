class Solution(object):
    def search(self, nums, target):
        l = len(nums)
        if l==0:
            return -1
        a,lo,hi=nums[0],0,l-1
        while lo<=hi:
            mid=(lo+hi)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target and nums[mid]>=a and target>=a:
                hi=mid-1
            elif nums[mid]>target and nums[mid]>=a and target<a:
                lo=mid+1
            elif nums[mid]>target and nums[mid]<a:
                hi=mid-1
            elif nums[mid]<target and nums[mid]>=a:
                lo=mid+1
            elif nums[mid]<target and nums[mid]<a and target>=a:
                hi=mid-1
            elif nums[mid]<target and nums[mid]<a and target<a:
                lo=mid+1
        return -1
            
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """