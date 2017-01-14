class Solution(object):
    def getRow(self, rowIndex):
        r = [0 for i in range(rowIndex+1)]
        r[0]=1
        for i in range(1,rowIndex+1):
            r[i]=1
            for j in range(i-1,0,-1):
                r[j]=r[j]+r[j-1]
        return r
        """
        :type rowIndex: int
        :rtype: List[int]
        """