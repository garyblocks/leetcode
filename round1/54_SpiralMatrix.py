class Solution(object):
    def spiralOrder(self, matrix):
        if matrix==[]:
            return []
        lc,lr = len(matrix[0])-1,len(matrix)-1
        s = 0
        r = []
        while lc>=0 and lr>=0:
            if lc==0:
                for a in range(lr+1):
                    r.append(matrix[s+a][s])
            elif lr==0:
                for b in range(lc+1):
                    r.append(matrix[s][s+b])
            else:
                for i in range(lc):
                    r.append(matrix[s][s+i])
                for i in range(lr):
                    r.append(matrix[s+i][lc+s])
                for i in range(lc):
                    r.append(matrix[lr+s][lc+s-i])
                for i in range(lr):
                    r.append(matrix[lr+s-i][s])
            lc-=2;lr-=2
            s+=1
        return r
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        “””