class Solution(object):
    def jump(self, nums):
        l = len(nums)
        if l<=1:
            return 0
        j = 0
        pos = [l for i in range(l)]
        pos[0]=0
        while j<l:
            if nums[j]+j+1>=l:
                return pos[j]+1
            t=1
            while j+t<l and nums[j]>=nums[j+t]+t:
                pos[j+t]=pos[j]+1
                t+=1
            k=t
            while j+k<l and k<=nums[j]:
                if pos[j+k]>pos[j]+1:
                    pos[j+k]=pos[j]+1
                    if j+k==l-1:
                        return pos[-1]
                k+=1
            j+=t
        return pos[-1]
        """
        :type nums: List[int]
        :rtype: int
        """