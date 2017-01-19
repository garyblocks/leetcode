class Solution(object):
    def candy(self, ratings):
        res = 0
        candy = 1
        prev = ratings[0]
        l = [[0,20000]]
        for i in range(len(ratings)):
            if ratings[i]>prev:
                prev=ratings[i]
                candy+=1
                l = [[i,20000]]
            elif ratings[i]<prev:
                if candy>1:
                    if candy>2:
                        l.append([i,candy-2])
                    candy=1
                else:
                    l[-1][1]-=1
                    res+=(i-l[-1][0])
                    if l[-1][1]==0:
                        l.pop()
                prev = ratings[i]
            else:
                l = [[i,20000]]
                candy=1
            res += candy
        return res
        """
        :type ratings: List[int]
        :rtype: int
        """