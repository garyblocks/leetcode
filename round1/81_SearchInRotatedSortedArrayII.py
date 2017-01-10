class Solution(object):
    def search(self, nums, target):
        lo,hi = 0, len(nums)-1
        left = True
        if target==nums[-1] or target==nums[0]:
            return True
        elif nums[0]>target>nums[-1]:
            return False
        elif target < nums[-1]:
            left=False
        cnt = 0
        while cnt<len(nums) and nums[0]==nums[-1]:
            nums.append(nums.pop(0))
            cnt+=1
        while lo<=hi:
            mid = lo+(hi-lo)/2
            if mid<0 or mid>=len(nums):
                break
            elif nums[mid]==target:
                return True
            elif nums[mid]<=nums[-1]:
                if nums[mid]>target:
                    hi=mid-1
                elif nums[mid]<target:
                    if left:
                        hi=mid-1
                    else:
                        lo=mid+1
            elif nums[mid]>=nums[0]:
                if nums[mid]>target:
                    if left:
                        hi=mid-1
                    else:
                        lo=mid+1
                elif nums[mid]<target:
                    lo=mid+1
        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """