class Solution(object):
    def find(self,w,b,i,j):
        if w=='':
            return True
        elif i>=len(b) or i<0 or j>=len(b[0]) or j<0:
            return False
        elif b[i][j]!=w[0]:
            return False
        else:
            t = b[i][j]
            b[i][j]='0'
            if (self.find(w[1:],b,i+1,j) 
                or self.find(w[1:],b,i-1,j) 
                or self.find(w[1:],b,i,j+1)
                or self.find(w[1:],b,i,j-1)):
                    return True
            b[i][j]=t
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (self.find(word,board,i,j)):
                    return True
        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """