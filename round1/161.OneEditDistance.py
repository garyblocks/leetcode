class Solution(object):
    def isOneEditDistance(self, s, t):
        flag = True
        s,t = s+'#',t+'#'
        i,j = 0,0
        while i<len(s) and j<len(t):
            print s[i],t[j]
            if s[i]!=t[j]:
                if flag:
                    flag = False
                else:
                    return False
                if j+1<len(t) and s[i]==t[j+1]:
                    j += 1
                elif i+1<len(s) and s[i+1]==t[j]:
                    i += 1
            i += 1
            j += 1
        if i<len(s) or j<len(t):
            return False
        return not flag
        """
        :type s: str
        :type t: str
        :rtype: bool
        """