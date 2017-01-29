class MinStack(object):
    def __init__(self):
        self.Stack=[]
        self.mins=[]
    def push(self, x):
        self.Stack.append(x)
        if len(self.mins)>0:
            if x<self.mins[0]:
                self.mins[0]=x
        else:
            self.mins.append(x)
    def pop(self):
        if self.Stack[-1]==self.mins[0]:
            self.mins.pop()
            if len(self.Stack)>1:
                self.mins.append(min(self.Stack[:-1]))
        self.Stack.pop()
    def top(self):
        return self.Stack[-1]
    def getMin(self):
        if len(self.mins)>0:
            return self.mins[0]
        else:
            return ''