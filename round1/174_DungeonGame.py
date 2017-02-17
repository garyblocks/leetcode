class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m,n = len(dungeon),len(dungeon[0])
        p = max(1,-dungeon[-1][-1]+1)
        health = [[0 for j in range(n)] for i in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    health[i][j] = p
                elif i==m-1:
                    if dungeon[i][j]>0:
                        health[i][j] = max(1,health[i][j+1]-dungeon[i][j])
                    else:
                        health[i][j] = health[i][j+1]-dungeon[i][j]
                elif j==n-1:
                    if dungeon[i][j]>0:
                        health[i][j] = max(1,health[i+1][j]-dungeon[i][j])
                    else:
                        health[i][j] = health[i+1][j]-dungeon[i][j]
                else:
                    tmp = min(health[i+1][j]-dungeon[i][j],health[i][j+1]-dungeon[i][j])
                    if dungeon[i][j]>0:
                        health[i][j] = max(1,tmp)
                    else:
                        health[i][j] = tmp
        return health[0][0]
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """