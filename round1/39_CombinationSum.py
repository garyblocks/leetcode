class Solution(object):
    def find(self,candidates,target,l,r,i):
        while i<len(candidates) and candidates[i]<=target:
            if candidates[i]==target:
                l.append(candidates[i])
                r.append(l)
            else:
                cp=l[:]
                cp.append(candidates[i])
                self.find(candidates,target-candidates[i],cp,r,i)
            i+=1
    def combinationSum(self, candidates, target):
        candidates.sort()
        r=[]
        l=[]
        index=0
        self.find(candidates,target,l,r,index)
        return r
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        “””