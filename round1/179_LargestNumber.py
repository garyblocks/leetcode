class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(item1, item2):
            i = 0
            a,b = len(item1),len(item2)
            while i<2*a or i<2*b:
                if item1[i%a]>item2[i%b]:
                    return 1
                elif item1[i%a]<item2[i%b]:
                    return -1
                else:
                    i+=1
            if a<b:
                return 1
            elif a>b:
                return -1
            else:
                return 0
        if sum(nums)==0:
            return '0'
        nums = list(map(str,nums))
        print compare('830','8308')
        nums = sorted(nums,reverse=True,cmp=compare)
        return ''.join(nums)