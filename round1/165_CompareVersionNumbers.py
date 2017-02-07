class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1,l2 = len(v1),len(v2)
        i,j = 0,0
        while i<l1 and j<l2:
            if int(v1[i])>int(v2[i]):
                return 1
            elif int(v1[i])<int(v2[i]):
                return -1
            i+=1;j+=1
        while j<l2:
            if int(v2[j])==0:
                j+=1
            else:
                return -1
        while i<l1:
            if int(v1[i])==0:
                i+=1
            else:
                return 1
        return 0
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """