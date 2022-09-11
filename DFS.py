
class Node:
    def __init__(self,data):
        self.data = data
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class DeapthFirstSearch:
    def DFS(self,startNode):
        stack = []
        stack.append(startNode)
        startNode.visited = True

        while stack:
            tempNode = stack.pop()
            print(tempNode.data,end=" ")
            for n in tempNode.adjacencyList:
                if n.visited is False:
                    n.visited = True
                    stack.append(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')


node1.adjacencyList.append(node2)
node1.adjacencyList.append(node5)
node2.adjacencyList.append(node3)
node2.adjacencyList.append(node4)


dfs = DeapthFirstSearch()
dfs.DFS(node1)



