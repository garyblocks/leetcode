class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        mat = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j]==1:
                    mat[i][j]=0
                elif i==0 and j==0:
                    mat[i][j]=1
                elif i==0:
                    mat[i][j]=mat[i][j-1]
                elif j==0:
                    mat[i][j]=mat[i-1][j]
                else:
                    mat[i][j]=mat[i-1][j]+mat[i][j-1]
        return mat[-1][-1]
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """