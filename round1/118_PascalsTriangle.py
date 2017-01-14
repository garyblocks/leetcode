class Solution(object):
    def generate(self, numRows):
        r = []
        for i in range(numRows):
            l=[]
            for j in range(i+1):
                if j==0 or j==i:
                    l.append(1)
                else:
                    l.append(r[i-1][j-1]+r[i-1][j])
            r.append(l)
        return r
        """
        :type numRows: int
        :rtype: List[List[int]]
        """