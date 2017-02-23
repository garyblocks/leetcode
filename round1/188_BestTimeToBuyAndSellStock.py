class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if k/2 >= n:
            res = 0
            for i in range(n-1):
                if prices[i]<prices[i+1]:
                    res += prices[i+1]-prices[i]
            return res
        table = [[0 for b in range(n)] for a in range(k+1)]
        for i in range(1,k+1):
            m = -prices[0]
            for j in range(1,n):
                table[i][j] = max(table[i][j-1],m+prices[j])
                m = max(m,table[i-1][j-1]-prices[j])
        return table[-1][-1]
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        