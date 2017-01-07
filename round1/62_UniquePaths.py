class Solution(object):
    def uniquePaths(self, m, n):
        mat=[[0 for j in range(n)] for i in range(m)]
        mat[0][0]=1
        for i in range(m):
            for j in range(n):
                if i>=1:
                    mat[i][j]+=mat[i-1][j]
                if j>=1:
                    mat[i][j]+=mat[i][j-1]
        return mat[-1][-1]
        """
        :type m: int
        :type n: int
        :rtype: int
        “””