class Solution(object):
    def subsetsWithDup(self, nums):
        r = []
        l = len(nums)
        sz = 2**l
        temp = [('0'*(l-len(bin(i)[2:]))+bin(i)[2:]) for i in range(sz)]
        for i in temp:
            t = []
            for j in range(l):
                if i[j]=='1':
                    t.append(nums[j])
            t.sort()
            if t not in r:
                r.append(t[:])
        return r        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """