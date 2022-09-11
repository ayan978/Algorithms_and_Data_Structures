class Node:
    def __init__(self, data):
        self.data = data
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None


class BreadthFirstSearch:
    def BFS(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            tempNode = queue.pop(0)
            tempNode.visited = True
            print(tempNode.data,end=" ")
            for n in tempNode.adjacencyList:
                if n.visited is False:
                    n.visited = True
                    queue.append(n)


n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')

n1.adjacencyList.append(n2)
n1.adjacencyList.append(n3)
n1.adjacencyList.append(n4)
n1.adjacencyList.append(n5)

bfs = BreadthFirstSearch()
bfs.BFS(n1)
