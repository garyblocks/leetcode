class Solution(object):
    def findSubstring(self, s, words):
        r = []; dic = {}
        if not words:
            return r
        else:
            l = len(words[0])
        for i in words:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        i = 0; w = len(words)
        while i<=(len(s)-w*l):
            if i+l<=len(s) and s[i:i+l] in dic:
                d = dic.copy()
                j = i
                while j+l<=len(s) and s[j:j+l] in d:
                    if d[s[j:j+l]] == 1:
                        d.pop(s[j:j+l])
                    else:
                        d[s[j:j+l]] -= 1
                    j+=l
                if not len(d):
                    r.append(i)
                i+=1
            else:
                i+=1
        return r
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """