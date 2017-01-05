class Solution(object):
    def trap(self, height):
        l = len(height)
        lo,hi= 0, l-1
        r = 0
        if l==0:
            return r
        a,b = height[lo],height[hi]
        while lo<hi:
            if height[lo]<=height[hi]:
                lo+=1
                if height[lo]<a:
                    r+=a-height[lo]
                else:
                    a = height[lo]
            else:
                hi-=1
                if height[hi]<=b:
                    r+=b-height[hi]
                else:
                    b=height[hi]
        return r
        """
        :type height: List[int]
        :rtype: int
        “””