class Solution(object):
    def isMatch(self, s, p):
        if s==p: 
            return True
        m,n = len(s), len(p)
        M = [[False for b in range(n+1)] for a in range(m+1)]
        M[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if i==0 and M[i][j-1] and ((j<n and p[j]=='*') or p[j-1]=='*'):
                    M[i][j]=True
                elif M[i][j-1]==True and (p[j-1]=='*' or (j<n and p[j]=='*')):
                    M[i][j]=True
                elif i>0 and M[i-1][j-1]==True and (p[j-1]==s[i-1] or p[j-1]=='.'):
                    M[i][j]=True
                elif i>0 and M[i-1][j]==True and ((j-1>0 and p[j-2]=='.' and p[j-1]=='*') or (j-1>0 and i-1>0 and p[j-2]==s[i-1] and p[j-1]=='*')):
                    M[i][j]=True
        return M[m][n]

        """
        :type s: str
        :type p: str
        :rtype: bool
        """