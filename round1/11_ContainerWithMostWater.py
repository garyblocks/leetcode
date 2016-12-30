class Solution(object):
    def maxArea(self, height):
        if len(height)<2:
            return 0
        i,j = 0,len(height)-1
        m = (j-i)*min(height[i],height[j])
        d1,d2=2,2
        while i+1!=j:
            d1-=1
            while height[i+d1]<=height[i] and i+d1+1<j:
                d1+=1
            else:
                a = (j-i-d1)*min(height[i+d1],height[j])
            d2-=1
            while height[j-d2]<=height[j] and j-d2-1>i:
                d2+=1
            else:
                b = (j-i-d2)*min(height[i],height[j-d2])
            if a>=b:
                i+=d1
                d1=2
            else:
                j-=d2
                d2=2
            if max(a,b)>m:
                m=max(a,b)
        return m
        
        """
        :type height: List[int]
        :rtype: int
        """