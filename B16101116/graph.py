
class Graph(object):
    def __init__(self,graph_dict=None):
        if graph_dict==None:
            graph_dict={}
        self.__graph_dict=graph_dict
    def vertices(self):
        return list(self.__graph_dict.keys())
    def find_edges(self):
        edges=[]
        for v in self.__graph_dict:
            for e in self.__graph_dict[v]:
                if {e,v} not in edges:
                    edges.append((v,e))
        return edges
    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex]=[]
        return
    def add_edge(self,vertex,edge):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex]=[]
            self.__graph_dict[vertex].append(edge)
        else:
            self.__graph_dict[vertex].append(edge)
def main():
    ob = {"a": ["c"],
          "b": ["c", "e"],
          "c": ["a", "b", "d", "e"],
          "d": ["c"],
          "e": ["c", "b"],
          "f": []
          }
    graph=Graph(ob)
    print("Printing Vertices of Graph")
    print(graph.vertices())
    print("Printing Edges of Graph")
    print(graph.find_edges())
    print("Adding Edges in Graph")
    graph.add_edge("a","d")
    print(graph.find_edges())

if __name__=="__main__":
     main()








