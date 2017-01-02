class Solution(object):
    def solve(self,row,col,grp,a,b,bd):
        if a==8 and b==8:
            del bd[:]
            for j in row:
                bd.append(j)
            return 
        elif b<8:
            b+=1
        else:
            a+=1;b=0
        if row[a][b]=='.':
            for k in range(1,10):
                t = str(k)
                if t not in col[b] and t not in row[a] and t not in grp[a/3*3+b/3]:
                    row1=[i[:] for i in row]
                    col1=[i[:] for i in col]
                    grp1=[i[:] for i in grp]
                    row1[a][b]=t; col1[b][a]=t; grp1[a/3*3+b/3][(a%3)*3+b%3]=t
                    self.solve(row1,col1,grp1,a,b,bd)
        else:
            self.solve(row,col,grp,a,b,bd)
                    
    def solveSudoku(self, board):
        row = board
        col,grp = [[] for a in range(10)],[[] for a in range(10)]
        for i in range(9):
            for j in range(9):
                col[j].append(row[i][j])
                grp[i/3*3+j/3].append(row[i][j])
        self.solve(row,col,grp,0,-1,board)
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """