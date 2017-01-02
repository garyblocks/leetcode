class Solution(object):
    def check(self,r,s):
        stack,cnt,new = 0,0,0
        flag = True
        step = 1
        for i in range(len(s)):
            if s[i]=='(':
                stack += 1
                if flag:
                    cnt += 1
                else:
                    new += 1
            elif stack:
                stack -= 1
                flag = False
                if new:
                    new-=1
                elif cnt:
                    cnt-=1
            else:
                step+=i
                break
            if not stack and r<i+1:
                r = i+1
        if cnt:
            step+=(cnt-1)
        return r,step
         
    def longestValidParentheses(self, s):
        l = len(s)
        i,r = 0,0
        while l-i>r and i<l:
            r,step = self.check(r,s[i:])
            i+=step
        return r
        """
        :type s: str
        :rtype: int
        """