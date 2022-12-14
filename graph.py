class Node:
    def __init__(self, id, name, descrpition, color):
        self.id = id
        self.name = name
        self.description = descrpition
        self.color = color

class Graph:
    def __init__(self):
        self.node_list = []
        self.edge_list = []
        
    def addNode(self, name = '', description = '', color = 'white'):
        node = Node(len(self.node_list), name, description, color)
        self.node_list.append(node)
        return node
    
    def setNode(self, node, color, description = ''):
        self.node_list[node.id].color = color
        self.node_list[node.id].descrpition = description
    
    def addEdge(self, parent, child, edgeValue = ''):
        self.edge_list.append({
            "parent": parent, 
            "child": child,
            "edge": edgeValue
            })
