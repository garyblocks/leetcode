class Solution(object):
    def maxSubArray(self, nums):
        l=len(nums)
        max = nums[0]
        for i in range(l):
            if nums[i]<=0:
                if nums[i]>max:
                    max=nums[i]
                continue
            else:
                sum = 0
                for j in range(i,l):
                    if sum<0:
                        break
                    else:
                        sum+=nums[j]
                        if sum>max:
                            max = sum
                    if j==(l-1):
                        return max
        return max
        """
        :type nums: List[int]
        :rtype: int
        """