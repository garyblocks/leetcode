class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        cur = lower
        tmp = ""
        r = []
        prev = -10000
        for i in nums:
            if i==prev:
                continue
            elif i==cur:
                cur += 1
                prev = i
            else:
                if i>cur+1:
                    r.append(str(cur)+"->"+str(i-1))
                else:
                    r.append(str(cur))
                cur = i+1
                prev = i
        if cur==upper:
            r.append(str(cur))
        elif cur<upper:
            r.append(str(cur)+"->"+str(upper))
        return r
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """