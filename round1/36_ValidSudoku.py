class Solution(object):
    def isValidSudoku(self, board):
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        grp = [[] for i in range(9)]
        s = {'1','2','3','4','5','6','7','8','9'}
        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c=='.':
                    continue
                elif c not in s:
                    return False
                else:
                    if c in row[i]:
                        print('f1',i,j)
                        return False
                    else:
                        row[i].append(c)
                    if c in col[j]:
                        print('f2',i,j)
                        return False
                    else:
                        col[j].append(c)
                    if c in grp[i/3*3+j/3]:
                        return False
                    else:
                        grp[i/3*3+j/3].append(c)
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """