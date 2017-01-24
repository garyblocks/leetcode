# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    import operator
    def maxPoints(self, points):
        def test(tup, p):
            n = [tup[1][1]-tup[0][1], tup[0][0]-tup[1][0]]
            v1 = [p.x-tup[0][0], p.y-tup[0][1]]
            v2 = [p.x-tup[1][0], p.y-tup[1][1]]
            dot1 = n[0]*v1[0]+n[1]*v1[1]
            dot2 = n[0]*v2[0]+n[1]*v2[1]
            if dot1==0 and dot2==0:
                return True
            else:
                return False
        n = len(points)
        if n==0: return 0
        elif n==1: return 1
        lines = {}
        for i in range(n):
            flag = True
            for j in lines:
                if test(j,points[i]):
                    lines[j] += 1
                    flag = False
            if flag:
                dup = {}
                for k in range(i):
                    t1 = (points[k].x,points[k].y)
                    if t1 in dup:
                        dup[t1] += 1
                    else:
                        dup[t1] = 2
                    t2 = (points[i].x,points[i].y)
                    lines[(t1,t2)] = dup[t1]
        sl = sorted(lines.items(), key=operator.itemgetter(1),reverse=True)
        return sl[0][1]
        """
        :type points: List[Point]
        :rtype: int
        """