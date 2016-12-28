class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        a=[nums1,nums2]
        if m>n:
            ia=0
        else:
            ia=1
        if min(m,n)==0 and (m+n)%2==1:
            return a[ia][(m+n)/2]
        if min(m,n)==0 and (m+n)%2==0:
            return (a[ia][(m+n)/2-1]+a[ia][(m+n)/2])/2.0 
        if (m+n)%2==1:
            l=int((m+n)/2+1)
            med=a[ia][l-1]
        else:
            l=(m+n)/2
            med=(a[ia][l-1]+a[abs(ia-1)][0])/2.0
        m1=l
        n1=0
        step=max(min(m,n)/2,1)
        print(med)
        while step>0:
            if a[ia][m1-1]>a[abs(1-ia)][n1]:
                m1-=step
                n1+=step
                if m1==0:
                    p=0
                else:
                    p=a[ia][m1-1]
                if p<a[abs(1-ia)][n1-1]:
                    ia=abs(1-ia)
                    t=m1
                    m1=n1
                    n1=t
                step=max(int(step/2),1)
                buf=min(m1,len(a[abs(1-ia)])-n1)
                step=min(buf,step)
            else:
                step=0
            if (m+n)%2==1:
                med=a[ia][m1-1]
            else:
                if m1>=len(a[ia]):
                    x=a[abs(1-ia)][n1]
                elif n1>=len(a[abs(1-ia)]):
                    x=a[ia][m1]
                else:
                    x=min(a[ia][m1],a[abs(1-ia)][n1])
                med=(a[ia][m1-1]+x)/2.0
            print(m1,n1,ia,step)
        return med
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """