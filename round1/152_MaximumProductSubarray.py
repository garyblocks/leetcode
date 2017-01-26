class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        i = 0
        while i<len(nums):
            if nums[i]==0:
                return max(self.maxProduct(nums[:i]),self.maxProduct(nums[i+1:]),0)
            i+=1
        neg = {}
        prod = 1
        prodp = 1
        for j in range(len(nums)):
            prodp *= nums[j]
            if nums[j]<0:
                neg[j]=prodp
            prod *= nums[j]
        print neg
        if len(neg)%2==1:
            maxp = 0
            for k in neg:
                if prod/neg[k]>maxp:
                    maxp = prod/neg[k]
                if neg[k]/nums[k]>maxp:
                    maxp = neg[k]/nums[k]
            return maxp
        else:
            return prod
        """
        :type nums: List[int]
        :rtype: int
        """