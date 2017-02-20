class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        def revS(s,a,b):
            n = b-a
            for i in range(n/2):
                s[a+i],s[a+n-1-i] = s[a+n-1-i],s[a+i]
        revS(s,0,len(s))
        start = 0
        for i in range(len(s)):
            if s[i]==' ':
                revS(s,start,i)
                start = i+1
        revS(s,start,len(s))