class Solution(object):
    def find(self,s,ind,r,t,st,l):
        if ind[1]==4:
            if ind[0]==l:
                r.append(st)
            return
        else:
            t.append(ind)
            if ind[0]<l:
                if ind[1]==0:
                    new=s[ind[0]]
                else:
                    new=st+'.'+s[ind[0]]
                self.find(s,(ind[0]+1,ind[1]+1),r,t,new,l)
            if ind[0]<l-1 and 9<int(s[ind[0]:ind[0]+2]):
                if ind[1]==0:
                    new=s[ind[0]:ind[0]+2]
                else:
                    new=st+'.'+s[ind[0]:ind[0]+2]
                self.find(s,(ind[0]+2,ind[1]+1),r,t,new,l)
            if ind[0]<l-2 and 99<int(s[ind[0]:ind[0]+3])<256:
                if ind[1]==0:
                    new=s[ind[0]:ind[0]+3]
                else:
                    new=st+'.'+s[ind[0]:ind[0]+3]
                self.find(s,(ind[0]+3,ind[1]+1),r,t,new,l)
    def restoreIpAddresses(self, s):
        l = len(s)
        ind=(0,0)
        r,t = [],[]
        st = ''
        self.find(s,ind,r,t,st,l)
        return r
        """
        :type s: str
        :rtype: List[str]
        “””