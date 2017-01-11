class Solution(object):
    def check(self,s1,s2,s3,i,j,k,s):
        if (i,j) in s:
            return False
        else:
            s.add((i,j))
        if k==len(s3):
            return True
        if len(s1)>i and s3[k]==s1[i]:
            i+=1;k+=1
            if self.check(s1,s2,s3,i,j,k,s):
                return True
            i-=1;k-=1
        if len(s2)>j and s3[k]==s2[j]:
            j+=1;k+=1
            if self.check(s1,s2,s3,i,j,k,s):
                return True
            j-=1;k-=1
        return False
    def isInterleave(self, s1, s2, s3):
        i,j,k=0,0,0
        s=set()
        if len(s1)+len(s2)==len(s3):
            return self.check(s1,s2,s3,i,j,k,s)
        else:
            return False
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """