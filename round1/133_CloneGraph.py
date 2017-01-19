# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def cp(nb,new,top):
            key = nb.label
            if key not in top:
                temp = UndirectedGraphNode(key)
                top[key] = temp
                new.neighbors.append(temp)
                for i in nb.neighbors:
                    cp(i,temp,top)
            else:
                new.neighbors.append(top[key])
        if not node:
            return None
        key = node.label
        new = UndirectedGraphNode(key)
        top = {key:new}
        for i in node.neighbors:
            cp(i,new,top)
        return new