class Graph: 
    def __init__(self, edges): 
        self.edges = edges 
        self.graph_dict = {}
        for i in self.edges: 
            if i[0] in self.graph_dict:
                self.graph_dict[i[0]].append(i[1])
            else: 
                self.graph_dict[i[0]] = [i[1]] 
    
    def get_paths(self, start, end, path = []):
        path = path + [start] 
        if start == end: 
            return [path]

        if start not in self.graph_dict: 
            return []
        
        paths = [] 

        for node in self.graph_dict[start]: 
            if node not in path: 
                new_paths = self.get_paths(node, end, path)
                for p in new_paths: 
                    paths.append(p)
        
        return paths
    
    def get_shortest_path(self, start, end, path=[]): 


        if start not in self.graph_dict: 
            return None
        
        paths = self.get_paths(start, end)
        shortestPath = paths[0]
        for i in self.get_paths(start, end): 
            if len(i) < len(shortestPath): 
                shortestPath = i 
        
        return shortestPath





routes = [
    ["Mumbai", "Paris"],
    ["Mumbai", "Dubai"],
    ["Paris", "Dubai"],
    ["Paris", "New York"],
    ["Dubai", "New York"],
    ["New York", "Toronto"]

]

route_graph = Graph(routes) 

print(route_graph.get_shortest_path("Mumbai", "New York"))