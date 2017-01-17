import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        bw,ew = {beginWord},{endWord}
        r = 1
        l = len(beginWord)
        while bw:
            r += 1
            temp = set()
            for word in bw:
                for i in range(l):
                    for c in string.lowercase:
                        if c != word[i]:
                            new = word[:i]+c+word[i+1:]
                            if new in ew:
                                return r
                            if new in wordList:
                                temp.add(new)
                                wordList.remove(new)
            bw = temp
            if len(ew)<len(bw):
                bw, ew = ew, bw
        return 0