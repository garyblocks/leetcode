class Solution(object):
    def wordBreak(self, s, wordDict):
        def help(s,f,dic):
            l = len(s)
            for i in range(l):
                if s[:i+1] in dic:
                    if i+1==l:
                        return True
                    elif s[i+1:] in f:
                        continue
                    elif help(s[i+1:],f,dic):
                        return True
                    else:
                        f.add(s[i+1:])
            return False
        f = set()
        return help(s,f,wordDict)
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """