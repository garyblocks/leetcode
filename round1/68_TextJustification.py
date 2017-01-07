class Solution(object):
    def fullJustify(self, words, maxWidth):
        r = []
        if not words:
            return [""]
        t = []; t.append([words[0]])
        L = maxWidth
        tmps,j = [len(words[0])],0
        for i in range(1,len(words)):
            if tmps[j] + len(words[i]) + 1 <= L:
                t[j].append(words[i])
                tmps[j] += (len(words[i]) + 1)
            else:
                t.append([words[i]])
                tmps.append(len(words[i]))
                j += 1
        for k in range(len(t)-1):
            even = ''
            if len(t[k])>1:
                l = len(t[k])-1
                even = (L-tmps[k])/l*' '
                odd = (L-tmps[k])%l
                for n in range(l+1):
                    if odd:
                        t[k][n] += ' '
                        odd -= 1
            r.append((' ' + even).join(t[k]))
        r.append((' ').join(t[len(t)-1]))
        for m in range(len(r)):
            if len(r[m]) < L:
                r[m] += (L-len(r[m]))*' '
        return r
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """