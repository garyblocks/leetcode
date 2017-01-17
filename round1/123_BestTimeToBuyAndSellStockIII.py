class Solution(object):
    def maxProfit(self, prices):
        sz = len(prices)
        fwd,near = [0],0
        for i in range(1,sz):
            if prices[i]<=prices[i-1]:
                fwd.append(fwd[i-1])
                if prices[i]<prices[near]:
                    near = i
            else:
                if prices[i]-prices[near]>fwd[i-1]:
                    fwd.append(prices[i]-prices[near])
                else:
                    fwd.append(fwd[i-1])
        bwd,near = [0],sz-1
        for i in range(sz-2,-1,-1):
            if prices[i]>=prices[i+1]:
                bwd.append(bwd[sz-i-2])
                if prices[i]>prices[near]:
                    near = i
            else:
                if prices[near]-prices[i]>bwd[sz-i-2]:
                    bwd.append(prices[near]-prices[i])
                else:
                    bwd.append(bwd[sz-i-2])
        bwd.reverse()
        print fwd
        print bwd
        k = max(fwd[-1],bwd[0])
        t = 0
        for j in range(sz-1):
            t = fwd[j]+bwd[j]
            if t>k:
                k = t
        return k
        """
        :type prices: List[int]
        :rtype: int
        """