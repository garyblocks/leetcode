class Solution(object):
    def longestCommonPrefix(self, strs):
        i = 0
        if strs==[]:
            return ''
        l = len(strs[i])
        o = ''; flag = False
        for k in strs:
            if len(k) < l:
                l = len(k)
        while i<l:
            for j in strs:
                if j[i] != strs[0][i]:
                    flag = True
            if flag:
                break
            o += strs[0][i]
            i += 1
        return o
        """
        :type strs: List[str]
        :rtype: str
        """