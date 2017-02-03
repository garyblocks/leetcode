# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.cache = []
    def read(self, buf, n):
        cnt = 0
        while n>0:
            if self.cache:
                buf[cnt] = self.cache.pop(0)
                cnt += 1
                n -= 1
                continue
            tbuf = [""]*4
            in4 = read4(tbuf)
            tmp = min(in4,n)
            for i in range(in4):
                if i<tmp:
                    buf[cnt+i] = tbuf[i]
                else:
                    self.cache.append(tbuf[i])
            cnt += tmp
            n -= 4
        return cnt
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        