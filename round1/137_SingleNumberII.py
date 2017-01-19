class Solution(object):
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]=1
            else:
                dic[i]=0
        for i in dic:
            if dic[i]==0:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """