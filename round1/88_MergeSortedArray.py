class Solution(object):
    def merge(self, nums1, m, nums2, n):
        new=[]
        i,j=0,0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
        if i==m:
            new=new+nums2[j:]
        elif j==n:
            new=new+nums1[i:]
        for k in range(m+n):
            nums1[k]=new[k]
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """