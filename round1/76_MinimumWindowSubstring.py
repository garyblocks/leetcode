class Solution(object):
    def minWindow(self, s, t):
        st = list(t)
        pos = []
        dic = {}
        l,start = len(s),-1
        for i in range(len(s)):
            if s[i] in st:
                if s[i] in dic:
                    dic[s[i]].append(i)
                else:
                    dic[s[i]]=[i]
                st.remove(s[i])
                pos.append(s[i])
                if start==-1:
                    start=i
            elif s[i] in dic:
                x=dic[s[i]].pop(0)
                dic[s[i]].append(i)
                pos.remove(s[i])
                pos.append(s[i])
                if s[i]==s[x]:
                    start=dic[pos[0]][0]
            if st==[]:
                l=i-start
                break
        if st:
            return ""
        m,n = l,start
        t = l+start+1
        for i in range(t,len(s)):
            if s[i]==pos[0]:
                pos.remove(s[i])
                pos.append(s[i])
                dic[s[i]].pop(0)
                dic[s[i]].append(i)
                start=dic[pos[0]][0]
                l=i-start
                if m>l:
                    m=l
                    n=start
            elif s[i] in dic:
                dic[s[i]].pop(0)
                dic[s[i]].append(i)
                pos.remove(s[i])
                pos.append(s[i])
        return s[n:n+m+1]        
        """
        :type s: str
        :type t: str
        :rtype: str
        """