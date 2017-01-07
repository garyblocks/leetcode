class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        if s=='':
            return False
        num={'1','2','3','4','5','6','7','8','9','0'}
        f,l = True,False
        punc={'.':True, '+':True, '-':True, 'e':True}
        i = 0 
        while i<len(s):
            t = s[i]
            if t in punc and punc[t]:
                punc[t]=False
                if t=='+' or t=='-':
                    if not f:
                        return False
                    else:
                        punc['+'],punc['-']=False,False
                elif t=='e':
                    if f:
                        return False
                    punc['.'],punc['+'],punc['-'],f,l=False,True,True,True,True
                else:
                    punc['+'],punc['-']=False,False
                i+=1
            elif t in num:
                if f:
                    f,l=False,False
                i+=1
            else:
                return False
        if l or f:
            return False
        return True
        """
        :type s: str
        :rtype: bool
        """