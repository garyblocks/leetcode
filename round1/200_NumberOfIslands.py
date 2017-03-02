class Solution(object):
    def numIslands(self, grid):
        labels = set()
        if not grid:
            return 0
        row,col = len(grid),len(grid[0])
        table = [[0 for j in range(col)] for i in range(row)]
        name = 1
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and i>0 and table[i-1][j]>0:
                    table[i][j]=table[i-1][j]
                elif grid[i][j]=='1' and (i==0 or table[i-1][j]==0):
                    name += 1
                    table[i][j]=name
                    labels.add(name)
            for j in range(col):
                if j>0 and table[i][j-1]>0 and table[i][j]>0 and table[i][j]!=table[i][j-1]:
                    a = max(table[i][j],table[i][j-1])
                    b = min(table[i][j],table[i][j-1])
                    for k in range(col):
                        if table[i][k]==a:
                            table[i][k]=b
                    labels.discard(a)
        return len(labels)
        """
        :type grid: List[List[str]]
        :rtype: int
        """