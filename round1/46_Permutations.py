class Solution(object):
    def pm(self,nums,r,t):
        for i in range(len(nums)):
            q = t[:]
            q.append(nums[i])
            if len(nums)==1:
                r.append(q)
            else:
                n = nums[:i]+nums[i+1:]
                self.pm(n,r,q)
        
    def permute(self, nums):
        r = []
        t = []
        self.pm(nums,r,t)
        return r
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        “””