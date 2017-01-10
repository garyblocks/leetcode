class Solution(object):
    def same(self,s1,s2):
        l1,l2=list(s1),list(s2)
        l1.sort();l2.sort()
        if l1==l2:
            return True
        else:
            return False
    def cut(self,s1,s2):
        poss=[]
        for i in range(1,len(s1)):
            if self.same(s1[:i],s2[:i]):
                poss.append([s1[:i],s1[i:],s2[:i],s2[i:]])
            if self.same(s1[:i],s2[-i:]):
                poss.append([s1[i:],s1[:i],s2[:-i],s2[-i:]])
        return poss
    def check(self,s1,s2):
        if s1==s2:
            return True
        else:
            li = self.cut(s1,s2)
            for i in li:
                a1,a2,b1,b2 = i
                if self.check(a1,b1) and self.check(a2,b2):
                    return True
            return False
    def isScramble(self, s1, s2):
        if not self.same(s1,s2):
            return False
        return self.check(s1,s2)
        
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """