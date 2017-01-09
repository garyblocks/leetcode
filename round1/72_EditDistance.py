class Solution(object):
    def minDistance(self, word1, word2):
        a,b = word1,word2
        l1,l2 = len(a),len(b)
        if a=='' or b=='':
            return max(l1,l2)
        M = [[(j+i) for j in range(l2+1)] for i in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                t=M[i-1][j-1]
                if a[i-1]==b[j-1]:
                    t=t-1
                M[i][j]=min(t+1,M[i-1][j]+1,M[i][j-1]+1)
        return M[-1][-1]
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """