class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        c = list(str(x))
        c.reverse()
        b = int(''.join(c))
        if x-b==0:
            return True
        else:
            return False