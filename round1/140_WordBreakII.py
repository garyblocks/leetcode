class Solution(object):
    def wordBreak(self, s, wordDict):
        dict = {}
        def find(s):
            if s in dict:
                return dict[s]
            tmp = []
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    if not s[i+1:]:
                        tmp.append([s[:i+1]])
                    elif find(s[i+1:]):
                        for j in find(s[i+1:]):
                            tmp.append([s[:i+1]]+j)
            dict[s] = tmp
            return tmp
        sol = find(s)
        res = []
        for i in sol:
            res.append(' '.join(i))
        return res
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """