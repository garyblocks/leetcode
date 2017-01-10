class Solution(object):
    def find(self,h):
        if h==[]:
            return 0
        low = min(h)
        l = len(h)
        area = low*l
        start = 0
        for i in range(l):
            if h[i]==low:
                area=max(self.find(h[start:i]),area)
                start=i+1
        if start<l:
            area=max(self.find(h[start:]),area)
        return area
    def find2(self,h):
        l=len(h)
        r = -1
        for k in h:
            if k*l>=r:
                r = k*l
            else:
                break
            l-=1
        return r
    def largestRectangleArea(self, heights):
        flag=True
        for k in range(len(heights)):
            if k+1<len(heights) and heights[k+1]<heights[k]:
                flag=False
        if heights and flag:
            return self.find2(heights)
        else:
            return self.find(heights)
        """
        :type heights: List[int]
        :rtype: int
        “””