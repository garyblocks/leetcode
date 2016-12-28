class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        if length == 1:
            return s
        lpodd = ''
        lpeven = ''
        indexodd = set(range(length))
        indexeven = set(range(length-1))
        step = 0
        delta = length/2+1
        while delta > 0:
            a = indexodd.copy()
            step += delta
            for i in a:
                if i-step >= 0 and i+step <= length-1:
                    substr = s[i-step:i+step+1]
                    if self.check(substr):
                        lpodd = substr
                    else:
                        indexodd.remove(i)
                else:
                    indexodd.remove(i)
            if len(indexodd) == 0 or step > (length-1)/2:
                indexodd = a
                step -= delta
                delta = delta/2
        step = 0
        delta = length/2
        c = indexeven.copy()
        for k in c:
            if s[k] != s[k+1]:
                indexeven.remove(k)
            else:
                lpeven = s[k:k+2]
        while delta > 0:
            b = indexeven.copy()
            step += delta
            for i in b:
                if i-step >= 0 and i+step+1 <= length-1:
                    substr = s[i-step:i+step+2]
                    if self.check(substr):
                        lpeven = substr
                    else:
                        indexeven.remove(i)
                else:
                    indexeven.remove(i)
            if len(indexeven) == 0 or step > length/2-1:
                indexeven = b
                step -= delta
                delta = delta/2
        if len(lpodd) > len(lpeven):
            lp = lpodd
        else:
            lp = lpeven
        return lp
    def check(self, s):
        l = len(s)
        if l == 1:
            return True
        for i in range(l/2):
            if s[i] != s[l-i-1]:
                return False
        return True