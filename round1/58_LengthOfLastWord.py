class Solution(object):
    def lengthOfLastWord(self, s):
        l = s.split()
        if l:
            return len(l[-1])
        return 0 
        """
        :type s: str
        :rtype: int
        “””