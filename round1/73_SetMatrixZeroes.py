class Solution(object):
    def setZeroes(self, matrix):
        if len(matrix)==0:
            return
        m = set()
        n = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    m.add(i)
                    n.add(j)
        for i in m:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in range(len(matrix)):
            for j in n:
                matrix[i][j]=0                
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """