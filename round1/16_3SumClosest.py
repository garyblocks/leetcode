class Solution(object):
    def threeSumClosest(self, nums, target):
        delta = abs(target-nums[0]-nums[1]-nums[2])
        out = 0
        nums.sort()
        for i in range(len(nums)-1):
            l,h = i+1,len(nums)-1
            while l<h:
                d = target-(nums[i]+nums[l]+nums[h])
                if d>0:
                    l+=1
                elif d<0:
                    h-=1
                else:
                    return target
                if abs(d) <= delta:
                    delta = abs(d)
                    out = target-d
        return out
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """