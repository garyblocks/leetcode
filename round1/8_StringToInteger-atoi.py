class Solution(object):
    def myAtoi(self, str):
        s = str
        num = list(s)
        num.reverse()
        digit={'0','1','2','3','4','5','6','7','8','9'}
        out = 0
        sign = 1
        l = len(s)
        count = False
        if l<1: 
            return out
        while l>=1:
            top = num[-1]
            if top not in digit:
                if count:
                    return out
                if top=='-':
                    num.pop()
                    sign=-1
                    l-=1
                    count=True
                elif top=='+':
                    num.pop()
                    l-=1
                    count=True
                elif top==' ':
                    num.pop()
                    l-=1
                else:
                    return out
            else:
                break
        if l<1:
            return out
        for i in range(l):
            if num[-1] not in digit:
                break
            out = 10*out+sign*int(num.pop())
        if out>2147483647:
            out=2147483647
        if out<-2147483648:
            out=-2147483648
        return out