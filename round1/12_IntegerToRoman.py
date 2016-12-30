class Solution(object):
    def intToRoman(self, num):
        s=''
        a1=num/1000; b1=num%1000
        for i in range(a1):
            s+='M'
        a2=b1/100; b2=b1%100
        if a2>=5 and a2<9:
            s+='D'
            for i in range(a2-5):
                s+='C'
        elif a2==9:
            s+='CM'
        elif a2==4:
            s+='CD'
        else:
            for i in range(a2):
                s+='C'
        a3=b2/10; b3=b2%10
        if a3>=5 and a3<9:
            s+='L'
            for i in range(a3-5):
                s+='X'
        elif a3==9:
            s+='XC'
        elif a3==4:
            s+='XL'
        else:
            for i in range(a3):
                s+='X'
        if b3>=5 and b3<9:
            s+='V'
            for i in range(b3-5):
                s+='I'
        elif b3==9:
            s+='IX'
        elif b3==4:
            s+='IV'
        else:
            for i in range(b3):
                s+='I'
        return s    
        """
        :type num: int
        :rtype: str
        """