class Solution(object):
    def find(self,t,r):
        temp = []
        for k in t:
            for i in range(len(k)):
                if i+1<len(k) and k[i]==k[i+1]:
                    new = k[:i]+[k[i]+k[i+1]]+k[i+2:]
                    if new not in temp:
                        temp.append(new)
                if i+2<len(k) and k[i]==k[i+2]:
                    new = k[:i]+[k[i]+k[i+1]+k[i+2]]+k[i+3:]
                    if new not in temp:
                        temp.append(new)
        if not temp:
            return
        else:
            for i in temp:
                if i not in r:
                    r.append(i)
            self.find(temp,r)
    def partition(self, s):
        t = [list(s)]
        r = t
        self.find(t,r)
        return r
        """
        :type s: str
        :rtype: List[List[str]]
        """