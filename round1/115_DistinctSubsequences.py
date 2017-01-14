class Solution(object):
    def numDistinct(self, s, t):
        dp = [[1 for i in range(len(s)+1)] for j in range(len(t)+1)]
        for i in range(1,len(t)+1):
            dp[i][0]=0
            for j in range(1,len(s)+1):
                if s[j-1]==t[i-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[-1][-1]
        """
        :type s: str
        :type t: str
        :rtype: int
        """