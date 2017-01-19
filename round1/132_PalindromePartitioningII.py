class Solution(object):
    def minCut(self, s):
        size = len(s)
        cut = [i-1 for i in range(size+1)]
        for i in range(size):
            for j in range(min(size-i,i+1)):
                if s[i-j] == s[i+j]:
                    cut[i+j+1] = min(cut[i+j+1],cut[i-j]+1)
                else: break
            for j in range(1,min(size-i,i+2)):
                if s[i-j+1] == s[i+j]:
                    cut[i+j+1] = min(cut[i+j+1],cut[i-j+1]+1)
                else: break
        return cut[-1]
        """
        :type s: str
        :rtype: int
        """