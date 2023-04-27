from vertex import Vertex
from graph import Graph

if __name__ == '__main__':
    G = Graph()
    input_edges = [
        (0,2),     
        (2,3),
        (3,1),     
        (1,0),     
    ]
    for edge in input_edges:
        if len(edge) < 3:
            w = 0
            s, d = edge
        else:
            s, d, w = edge
        G.addEdge(s, d, w)

    print(G.isCyclic())