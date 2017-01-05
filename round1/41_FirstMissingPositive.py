class Solution(object):
    def firstMissingPositive(self, nums):
        min,max,cnt,sum = 2147483647,0,0,0
        for i in nums:
            if i>=1:
                cnt+=1; sum+=i
                if i<min: min=i
                if i>max: max=i
        if max==0:
            return 1
        if min-1>0:
            return 1
        elif max == cnt and (min+max)*cnt/2==sum:
            return max+1
        else:
            full=0
            for k in range(cnt,0,-1):
                full=full*10+k
            new=0
            for j in nums:
                if 0<j<=cnt and (new/10**(j-1))%10==0:
                    new+=j*10**(j-1)
            delta = full-new
            for k in range(1,cnt+1):
                if delta%(10**k)>0:
                    return k
        """
        :type nums: List[int]
        :rtype: int
        """