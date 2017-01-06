class Solution(object):
    def find(self,r,col,pos,neg,i,n):
        if i==n:
            r[0]+=1; return
        else:
            for j in range(n):
                if (col[j] and pos[i+j] and neg[n-i+j-1]):
                    col[j],pos[i+j],neg[n-i+j-1]=False,False,False
                    self.find(r,col,pos,neg,i+1,n)
                    col[j],pos[i+j],neg[n-i+j-1]=True,True,True
        
    def totalNQueens(self, n):
        r = [0]
        col = [True for a in range(n)]
        pos = [True for a in range(2*n-1)]
        neg = [True for a in range(2*n-1)]
        self.find(r,col,pos,neg,0,n)
        return r[0]
        """
        :type n: int
        :rtype: int
        """