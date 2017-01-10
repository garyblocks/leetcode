class Solution(object):
    def find(self,vec):
        r = 0
        stack = []
        start=0
        i = 0
        while i<len(vec):
            if not stack or vec[i]>=vec[stack[-1]]:
                stack.append(i)
                i+=1
                continue
            while stack and vec[i]<vec[stack[-1]]:
                h=vec[stack.pop()]
                if stack:
                    l=i-stack[-1]-1
                else:
                    l=i-start
                r=max(r,l*h)
        while stack:
            h=vec[stack.pop()]
            if stack:
                l=i-stack[-1]-1
            else:
                l=i-start
            r=max(r,l*h)
        return r
                
    def maximalRectangle(self, matrix):
        r = 0
        if matrix==[]:
            return r
        vec = [0 for i in range(len(matrix[0])+1)]
        for i in matrix:
            for j in range(len(i)):
                if i[j]=='1':
                    vec[j]+=1
                else:
                    vec[j]=0
            r = max(r,self.find(vec))
        return r        
        """
        :type matrix: List[List[str]]
        :rtype: int
        """