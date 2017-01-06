import copy
class Solution(object):
    def update(self,ck,i,j,n):
        for a in range(n):
            ck[i][a] = False
        for b in ck:
            b[j] = False
        c,d = i,j
        while c<n and d<n: ck[c][d]=False; c+=1; d+=1
        c,d = i,j
        while c<n and d>=0: ck[c][d]=False; c+=1; d-=1
        c,d = i,j
        while c>=0 and d>=0: ck[c][d]=False; c-=1; d-=1
        c,d = i,j
        while c>=0 and d<n: ck[c][d]=False; c-=1; d+=1
        
    def find(self,r,tmp,ck,n,q,i,j):
        j = 0
        while j<n:
            if ck[i][j]==True and q>0:
                tmp[i][j]='Q'
                if q==1:
                    new = []
                    for k in tmp:
                        new.append(''.join(k))
                    r.append(new)
                q-=1
                snap = copy.deepcopy(ck)
                self.update(ck,i,j,n)
                if q>0:
                    s,g = i+1,j
                    self.find(r,tmp,ck,n,q,s,g)
                q+=1; ck = snap; tmp[i][j]='.'
            j+=1
                
    def solveNQueens(self, n):
        r = []
        tmp = [['.' for a in range(n)] for b in range(n)]
        ck = [[True for a in range(n)] for b in range(n)]
        q = n
        i,j = 0,0
        self.find(r,tmp,ck,n,q,i,j)
        return r
        """
        :type n: int
        :rtype: List[List[str]]
        """