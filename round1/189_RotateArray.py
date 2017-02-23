class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        t=nums[n-k:]
        for i in range(n-k-1,-1,-1):
            nums[i+k]=nums[i]
        nums[:k]=t
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """