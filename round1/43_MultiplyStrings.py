class Solution(object):
    def multiply(self, num1, num2):
        if num1[0]=='0' or num2[0]=='0':
            return str(0)
        result=[]
        for i in range(len(num1)-1,-1,-1):
            temp,m = 0,1
            for j in range(len(num2)-1,-1,-1):
                temp += (int(num1[i])*int(num2[j])*m)
                m *= 10
            result.append(temp)
        r,n = 0,1
        for j in result:
            r += j*n
            n *= 10
        return str(r)
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """