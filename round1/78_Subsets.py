class Solution(object):
    def sub(self,n,r,lo,hi,l):
        r.append(l)
        if lo==hi:
            return
        for j in range(lo,hi):
            new=l+[n[j]]
            self.sub(n,r,j+1,hi,new)
            
    def subsets(self, nums):
        sz = len(nums)
        r = []
        self.sub(nums,r,0,sz,[])
        return r
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """