class Solution(object):
    def strStr(self, haystack, needle):
        l1 = len(haystack)
        l2 = len(needle)
        i = 0
        if l2>l1 or l2==[]:
            return -1
        while i<=l1-l2:
            if needle==haystack[i:i+l2]:
                return i
            else:
                i+=1
        return -1
            
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """