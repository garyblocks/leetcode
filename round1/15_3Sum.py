class Solution(object):
    def threeSum(self, nums):
        a,b,c = [],[],[]
        result = []
        for i in nums:
            if i>0:
                c.append(i)
            elif i<0:
                a.append(i)
            else:
                b.append(i)
        d,e = set(a),set(c)
        if len(b)>=3:
            result.append([0,0,0])
        if len(b)>0:
            for i in d:
                for j in e:
                    if i+j==0:
                        result.append([i,0,j])
        for i in d:
            for j in range(len(c)):
                for k in c[j+1:len(c)]:
                    if i+c[j]+k==0:
                        t = [i,c[j],k]; t.sort()
                        if t not in result:
                            result.append(t)
        for i in e:
            for j in range(len(a)):
                for k in a[j+1:len(a)]:
                    if i+a[j]+k==0:
                        t = [a[j],k,i]; t.sort()
                        if t not in result:
                            result.append(t)
        return(result)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """