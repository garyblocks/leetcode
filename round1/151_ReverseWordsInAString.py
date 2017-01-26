class Solution(object):
    def reverseWords(self, s):
        l = s.split()
        l.reverse()
        return ' '.join(l)
        """
        :type s: str
        :rtype: str
        """