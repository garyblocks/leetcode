import re
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        lst=re.split('\W+',s)
        s=''.join(lst)
        s.strip()
        l = len(s)
        for i in range(l/2):
            if s[i]!=s[-i-1]:
                return False
        return True
        """
        :type s: str
        :rtype: bool
        """