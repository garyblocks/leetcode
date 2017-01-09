class Solution(object):
    def searchrow(self,m,t):
        l = len(m)
        lo,hi = 0,l-1
        while lo<=hi:
            mid = lo+(hi-lo)/2
            if m[mid][0]>t:
                hi=mid-1
            elif mid<l-1 and m[mid+1][0]<=t:
                lo=mid+1
            else:
                return mid
        return -1
    def searchcol(self,ls,t):
        l = len(ls)
        lo,hi = 0, l-1
        while lo<=hi:
            mid = lo+(hi-lo)/2
            if ls[mid]>t:
                hi=mid-1
            elif ls[mid]<t:
                lo=mid+1
            else:
                return True
        return False
    def searchMatrix(self, matrix, target):
        row = self.searchrow(matrix,target)
        if row<0:
            return False
        else:
            return self.searchcol(matrix[row],target)
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """