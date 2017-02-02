# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        cnt = 0
        while n>0:
            tbuf = [""]*4
            tmp = min(read4(tbuf),n)
            j = 0
            for i in range(cnt,cnt+tmp):
                buf[i] = tbuf[j]
                j += 1
                cnt += 1
            n -= 4
        return cnt
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """