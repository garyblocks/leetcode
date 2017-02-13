class Solution(object):
    def titleToNumber(self, s):
        r = 0
        for i in s:
            r=r*26+ord(i)-64
        return r
        """
        :type s: str
        :rtype: int
        """