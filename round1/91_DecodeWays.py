class Solution(object):
    def check(self,s,dic):
        if s in dic:
            a = dic[s]
        else:
            a = self.count(s,dic)
            dic[s] = a
        return a
    def count(self,n,dic):
        sz = len(n)
        if sz<=1:
            return 1
        elif n[0]=='1':
            return self.check(n[1:],dic)+self.check(n[2:],dic)
        elif n[0]=='2' and int(n[1])<7:
            return self.check(n[1:],dic)+self.check(n[2:],dic)
        else:
            return self.check(n[1:],dic)
    def numDecodings(self, s):
        l,dic = len(s),{}
        if s=='':
            return 0
        n,j='',0
        while j<l:
            if s[j]=='0':
                return 0
            elif (s[j]=='1' or s[j]=='2') and j<l-1 and s[j+1]=='0':
                j+=2
            else:
                n+=s[j]
                j+=1
        result = self.count(n,dic)
        return result
        """
        :type s: str
        :rtype: int
        """