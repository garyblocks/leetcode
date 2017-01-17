class Solution(object):
    def maxProfit(self, prices):
        l = len(prices)
        r = 0
        if l<=1:
            return r
        lo=prices[0]
        for i in range(l):
            if i+1<l and prices[i+1]>=prices[i] and i>0 and prices[i-1]>prices[i]:
                if prices[i]<lo:
                    lo=prices[i]
            elif i>0 and prices[i-1]<=prices[i] and ((i+1<l and prices[i+1]<prices[i]) or i==l-1):
                if prices[i]-lo>r:
                    r=prices[i]-lo
        return r       
        """
        :type prices: List[int]
        :rtype: int
        """