from collections import defaultdict

class DFSTraversal:
    def _init_(self, v):
        self.vertex = v
        self.adj = defaultdict(list)

    def insert_edge(self, v, w):
        self.adj[v].append(w)

    def DFSUtil(self, n, nodes):
        nodes[n] = True
        print(n, end=" ")

        for a in self.adj[n]:
            if not nodes[a]:
                self.DFSUtil(a, nodes)

    def DFS(self, n):
        nodes = [False] * self.vertex
        self.DFSUtil(n, nodes)

if _name_ == "_main_":
    graph = DFSTraversal(10)
    graph.insert_edge(0, 1)
    graph.insert_edge(0, 2)
    graph.insert_edge(0, 3)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 4)
    graph.insert_edge(3, 5)
    graph.insert_edge(3, 6)
    graph.insert_edge(4, 7)
    graph.insert_edge(4, 5)
    graph.insert_edge(5, 2)
    graph.insert_edge(6, 5)
    graph.insert_edge(7, 5)
    graph.insert_edge(7, 8)

    print("Depth First Traversal for the graph is:")
    graph.DFS(2)
