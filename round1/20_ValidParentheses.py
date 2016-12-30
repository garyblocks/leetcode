class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {'(':')','{':'}','[':']'}
        for i in s:
            if i in dic:
                stack.append(dic[i])
            elif not stack:
                return False
            elif i!=stack.pop():
                return False
        if not stack:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """