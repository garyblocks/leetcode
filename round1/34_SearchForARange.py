class Solution(object):
    def searchRange(self, nums, target):
        r = [-1,-1]
        if not nums:
            return r
        lo,hi = 0, len(nums)-1
        while lo<=hi:
            mid = (lo+hi)/2
            if nums[mid]<target:
                lo=mid+1
            elif nums[mid]>target:
                hi=mid-1
            else:
                if nums[lo]==target:
                    lm=lo
                else:
                    lm=(lo+mid)/2
                    while lo<=lm:
                        if nums[lm]<target:
                            lo = lm
                            lm = max((lo+mid)/2,lo+1)
                        elif nums[lm-1]<target:
                            break
                        else:
                            lm = (lo+lm)/2
                if nums[hi]==target:
                    hm=hi
                else:
                    hm=(mid+hi)/2
                    while hi>=hm:
                        if nums[hm]>target:
                            hi = hm
                            hm = (hi+mid)/2
                        elif nums[hm+1]>target:
                            break
                        else:
                            hm = (hi+hm)/2
                    
                r=[lm,hm]
                break
        return r
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """