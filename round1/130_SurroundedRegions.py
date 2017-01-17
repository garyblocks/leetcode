class Solution(object):
    def solve(self, board):
        def update(i,j,board,status,row,col):
            status[i][j]=False
            if i-1>0 and status[i-1][j] and board[i-1][j]=='O':
                update(i-1,j,board,status,row,col)
            if j-1>0 and status[i][j-1] and board[i][j-1]=='O':
                update(i,j-1,board,status,row,col)
            if i+1<row and status[i+1][j] and board[i+1][j]=='O':
                update(i+1,j,board,status,row,col)
            if j+1<col and status[i][j+1] and board[i][j+1]=='O':
                update(i,j+1,board,status,row,col)
        if not board:
            return
        row,col = len(board),len(board[0])
        status = [[True for j in range(col)] for i in range(row)]
        for i in range(col):
            if board[0][i]=='O' and status[0][i]:
                update(0,i,board,status,row,col)
        for i in range(row):
            if board[i][col-1]=='O' and status[i][col-1]:
                update(i,col-1,board,status,row,col)
        for i in range(col):
            if board[row-1][i]=='O' and status[row-1][i]:
                update(row-1,i,board,status,row,col)
        for i in range(row):
            if board[i][0]=='O' and status[i][0]:
                update(i,0,board,status,row,col)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and status[i][j]:
                    board[i][j]='X'
        return 
        
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """