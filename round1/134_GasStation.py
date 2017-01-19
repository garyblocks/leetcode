class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        l = len(gas)
        new = 0
        temp = 0
        s = 0
        for i in range(l):
            s += gas[i]-cost[i] 
            new += gas[i]-cost[i]
            if new<0:
                temp = i+1
                new = 0
        if s<0:
            return -1
        else:
            return temp
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """