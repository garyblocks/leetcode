class Solution(object):
    def perm(self,r,nums,i,tmp,l):
        if i==l:
            t = tmp[:]
            r.append(t)
            return
        else:
            p = 's'
            for j in nums:
                if j==p:
                    continue
                tmp.append(j)
                new = nums[:]
                new.remove(j)
                k = tmp[:]
                self.perm(r,new,i+1,k,l)
                tmp.pop()
                p = j
            
    def permuteUnique(self, nums):
        nums.sort()
        r = []
        if nums == []:
            return r
        else:
            tmp = []; l=len(nums)
            self.perm(r,nums,0,tmp,l)
        return r
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        “””