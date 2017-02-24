class Solution(object):
    def hammingWeight(self, n):
        cnt = 0
        s = bin(n)[2:]
        for i in s:
            if i=='1':
                cnt+=1
        return cnt
        """
        :type n: int
        :rtype: int
        """