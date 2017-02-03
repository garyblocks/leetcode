class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0
        left,mid = 0,-1
        first,second = s[0],''
        r = 0
        for i in range(len(s)):
            if s[i]==second:
                r = max(r,i-left+1)
            elif s[i]==first:
                if mid>0:
                    first,second = second,first
                    mid = i
                r = max(r,i-left+1)
            else:
                if mid<0:
                    mid = i
                else:
                    left = mid
                    mid = i
                    first = second
                second = s[i]
                r = max(r,i-left+1)
        return r
        """
        :type s: str
        :rtype: int
        """
        