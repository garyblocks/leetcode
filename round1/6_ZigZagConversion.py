class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        letters = []
        block = 2*numRows-2
        length = len(s)
        for j in range(numRows):
            letters.append([])
        for i in range(length):
            q = i%block
            if q < numRows-1:
                letters[q].append(s[i])
            else:
                letters[block-q].append(s[i])
        new=''
        for t in letters:
            a = ''.join(t)
            new += a
        return new
