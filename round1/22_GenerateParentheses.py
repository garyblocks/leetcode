class Solution(object):
    def add(self,out,n,check,num,s,p,left,right):
        if p=='(':
            s+=p; check-=1; num+=1; left-=1
        elif check<0:
            s+=p; check+=1; num+=1; right-=1
        else:
            return None
        if num<2*n:
            if left>0:
                self.add(out,n,check,num,s,'(',left,right)
            if right>0:
                self.add(out,n,check,num,s,')',left,right)
        else:
            out.append(s)
            
    def generateParenthesis(self, n):
        out = []
        check = 0
        num = 0
        left, right = n,n
        s = ''
        self.add(out,n,check,num,s,'(',left,right)
        return out
        """
        :type n: int
        :rtype: List[str]
        """