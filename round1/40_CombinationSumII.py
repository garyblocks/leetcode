class Solution(object):
    def find(self,c,r,t,a):
        sum = 0
        i = 0
        l = len(c)
        while i<l:
            if (sum+c[i])==t:
                a.append(c[i])
                r.append(a)
                break
            elif (sum+c[i])<t:
                b = a[:]
                b.append(c[i])
                j = t-c[i]
                i+=1; d=c[i:]
                self.find(d,r,j,b)
            else:
                break
            while i<l and c[i]==c[i-1]:
                i+=1
                
    def combinationSum2(self, candidates, target):
        r = []
        a = []
        candidates.sort()
        l = len(candidates)
        self.find(candidates,r,target,a)
        return r
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """