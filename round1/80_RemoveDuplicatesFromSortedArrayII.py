class Solution(object):
    def removeDuplicates(self, nums):
        cnt,i = 0,0
        while i<len(nums):
            if i>0 and nums[i]==nums[i-1]:
                cnt+=1
                if cnt>=3:
                    nums.pop(i)
                else:
                    i+=1
            else:
                cnt=1
                i+=1
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """