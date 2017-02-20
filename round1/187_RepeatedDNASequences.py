class Solution(object):
    def findRepeatedDnaSequences(self, s):
        dic = {(ord('G')-ord('A')):1,(ord('T')-ord('A')):2,(ord('C')-ord('A')):3,0:0}
        word,dup = set(),set()
        r = []
        w = 0
        for i in range(len(s)):
            if i<9:
                w = w>>2
                w |= dic[(ord(s[i])-ord('A'))]<<18
                continue
            else:
                w = w>>2
                w |= dic[(ord(s[i])-ord('A'))]<<18
            if w in word and w not in dup:
                r.append(s[i-9:i+1])
                dup.add(w)
            else:
                word.add(w)
        return r
        """
        :type s: str
        :rtype: List[str]
        """