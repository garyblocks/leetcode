class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        start = {beginWord}
        dic = {beginWord:[[beginWord]]}
        while True:
            temp = set()
            for word in start:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c!=word[i]:
                            new = word[:i]+c+word[i+1:]
                        else:
                            continue
                        if new in wordlist:
                            if new not in temp:
                                temp.add(new)
                                dic[new]=[]
                            for k in dic[word]:
                                p = k[:]
                                p.append(new)
                                dic[new].append(p)
            if endWord in temp:
                return dic[endWord]
            elif not temp:
                return []
            wordlist = wordlist - temp
            start = temp
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """