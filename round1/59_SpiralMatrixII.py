class Solution(object):
    def generateMatrix(self, n):
        r = [[0 for i in range(n)] for i in range(n)]
        l,s = n-1,0
        m = 1
        q = n*n
        while l>=0 and m<=q:
            if l==0:
                r[s][s]=m
                return r
            for i in range(l):
                r[s][s+i]=m; m+=1
            for i in range(l):
                r[s+i][l+s]=m; m+=1
            for i in range(l):
                r[l+s][l+s-i]=m; m+=1
            for i in range(l):
                r[l+s-i][s]=m; m+=1
            s+=1;l-=2
        return r
        """
        :type n: int
        :rtype: List[List[int]]
        """