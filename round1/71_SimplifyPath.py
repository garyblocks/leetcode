class Solution(object):
    def simplifyPath(self, path):
        dirl=path.split('/')
        s=[]
        for i in dirl:
            if i=='' or i=='.':
                continue
            elif i=='..':
                if len(s)>0:
                    s.pop()
            else:
                s.append(i)
        return '/'+'/'.join(s)
        """
        :type path: str
        :rtype: str
        """