class Solution(object):
    def isMatch(self, s, p):
        if s==p:
            return True
        elif p=='':
            return False
        else:
            c = 0
            for t in p:
                if t!='*':
                    c+=1
            if c>len(s):
                return False
            DP = [[False for b in range(len(p)+1)] for a in range(len(s)+1)]
            DP[0][0] = True
            for i in range(len(s)+1):
                for j in range(1,len(p)+1):
                    if DP[i][j-1]==True and p[j-1]=='*':
                        DP[i][j] = True
                    elif i>0 and DP[i-1][j]==True and p[j-1]=='*':
                        DP[i][j] = True
                    elif i>0 and DP[i-1][j-1]==True and (s[i-1]==p[j-1] or p[j-1]=='?' or p[j-1]=='*'):
                        DP[i][j] = True
            if DP[len(s)][len(p)]==True:
                return True
            else:
                return False
        """
        :type s: str
        :type p: str
        :rtype: bool
        “””