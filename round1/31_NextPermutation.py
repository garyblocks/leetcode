class Solution(object):
    def nextPermutation(self, nums):
        l = len(nums)
        i = l-1
        if l<2:
            return
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            nums.sort()
            return
        pivot = i-1
        j = i;t = j
        while j<l:
            if nums[j]>nums[pivot]:
                t=j
                j+=1
            else:
                break
        nums[pivot],nums[t]=nums[t],nums[pivot]
        while i!= l-1:
            for j in range(i,l-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
            l-=1
                
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """