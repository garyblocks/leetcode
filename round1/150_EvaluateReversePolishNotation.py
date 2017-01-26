import math
class Solution(object):
    def evalRPN(self, tokens):
        ops = {"+","-","*","/"}
        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(i)
            else:
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                if i=="+":
                    stack.append(v1+v2)
                elif i=="-":
                    stack.append(v2-v1)
                elif i=="*":
                    stack.append(v1*v2)
                elif i=="/":
                    stack.append(int(float(v2)/v1))
        return int(stack.pop())    
        """
        :type tokens: List[str]
        :rtype: int
        """