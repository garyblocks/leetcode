class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        i = 0
        while i < n/2:
            for j in range(n):
                matrix[i][j],matrix[n-1-i][j]=matrix[n-1-i][j],matrix[i][j]
            i += 1
        c = 1
        for a in range(n-1):
            for b in range(c,n):
                matrix[a][b],matrix[b][a]=matrix[b][a],matrix[a][b]
            c += 1
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """