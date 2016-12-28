class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        i,j=0,0
        flag=False
        copy=list(nums)
        copy.sort()
        p,q=0,len(copy)-1
        while True:
            sum = copy[p]+copy[q]
            if sum>target:
                q-=1
            elif sum<target:
                p+=1
            else:
                i=nums.index(copy[p])
                nums[i]=.5
                j=nums.index(copy[q])
                break
        l.append(i)
        l.append(j)
        return l
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """