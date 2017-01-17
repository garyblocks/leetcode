class Solution(object):
    def maxProfit(self, prices):
        r = 0
        for i in range(len(prices)):
            if i+1<len(prices) and prices[i+1]>prices[i]:
                r += prices[i+1]-prices[i]
        return r
        """
        :type prices: List[int]
        :rtype: int
        """