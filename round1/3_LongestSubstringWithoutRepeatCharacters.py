class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=[]
        m=0
        for i in range(len(s)):
            if s[i] in l:
                m=max(m,len(l))
                low=l.index(s[i])+1
                l=l[low:]
                l.append(s[i])
            else:
                l.append(s[i])
        m=max(m,len(l))
        return m
        """
        :type s: str
        :rtype: int
        """