class Solution(object):
    def twoSum(self,nums,target,i,j,out):
        l = len(nums)
        a,b = 0,l-1
        while a<b:
            if nums[a]+nums[b]<target:
                while a+1<b and nums[a]==nums[a+1]:
                    a+=1
                a+=1
            elif nums[a]+nums[b]>target:
                while b-1>a and nums[b]==nums[b-1]:
                    b-=1
                b-=1
            else:
                out.append([i,nums[a],nums[b],j])
                while a+1<b and nums[a]==nums[a+1]:
                    a+=1
                while b-1>a and nums[b]==nums[b-1]:
                    b-=1
                a+=1; b-=1;
                
    def fourSum(self, nums, target):
        nums.sort()
        out = []
        l = len(nums)
        if l<4:
            return out
        for i in range(l-3):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(l-1,i+2,-1):
                if j+1<l and nums[j+1]==nums[j]:
                    continue
                self.twoSum(nums[i+1:j],target-nums[i]-nums[j],nums[i],nums[j],out)
        return out
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """