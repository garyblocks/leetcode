class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        n = 0
        r = []
        for k in strs:
            l = list(k)
            l.sort()
            s = ''.join(l)
            if s in dic:
                r[dic[s]].append(k)
            else:
                dic[s]=n
                r.append([k])
                n+=1
        return r
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        “””