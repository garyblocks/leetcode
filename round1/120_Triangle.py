class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        lst = [0 for i in range(n)]
        lst[0] = triangle[0][0]
        for i in range(1,n):
            prev = lst[:]
            j = 0
            lst[j] = prev[j]+triangle[i][j]
            j+=1
            while j < i:
                lst[j]=triangle[i][j]+min(prev[j-1],prev[j])
                j+=1
            lst[j] = prev[j-1]+triangle[i][j]
            print lst
        return min(lst)
                
        """
        :type triangle: List[List[int]]
        :rtype: int
        """