class Solution(object):
    def majorityElement(self, nums):
        d = {}
        l = int((len(nums)+1)/2)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]>=l:
                return i
        """
        :type nums: List[int]
        :rtype: int
        “””