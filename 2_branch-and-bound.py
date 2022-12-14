import time
from graph import Graph, Node
import copy

testCaseNo = 0

W = 0
N = 10005
m = 0 
n = 0
bestOfLabel = []
arr = []

class TreeNode:
    def __init__(self, weight = 0, value = 0, index = -1, label = 0):
        self.weight = weight
        self.value = value
        if weight != 0:
            self.ratio = value / weight
        else:
            self.ratio = 0
        self.index = index
        self.label = label

    def __str__(self):
        return "class<TreeNode> weight: " + str(self.weight) +\
           ", value: " + str(self.value) +\
           ", ratio: " + str(self.ratio) +\
           ", label: " + str(self.label)
        
    
def input():
    global W, m
    global n
    global arr, bestOfLabel
    with open(f'./input/Input_{testCaseNo}.txt', 'r') as f:
        W = int(f.readline())
        m = int(f.readline())
        weights = f.readline().split(', ')
        values = f.readline().split(', ')
        labels = f.readline().split(', ')
        n = len(labels)
        i = 0
        for w, v, c in zip(weights, values, labels):
            arr.append(TreeNode(int(w), int(v), int(i), int(c)))
            i += 1
        

class BranchNode:
    def __init__(self, node):
        self.treeNode = node
        self.cumW = node.weight
        self.cumV = node.value
        self.label_set = set()
        self.label_set.add(node.label)
        self.flag = []
        self.level = node.index
        self.flag.append(node.index)

    def bound(self):
        global n
        global W
        node = copy.deepcopy(self)
        for index in range(node.level + 1, n):
            if arr[index].weight + node.cumW <= W:
                node.cumW += arr[index].weight
                node.cumV += arr[index].value
                node.label_set.add(arr[index].label)
        if len(node.label_set) < m:
            return -1
        return node.cumV
    
    def isValid(self):
        global W
        return self.cumW <= W
        
class BranchAndBound:
    def __init__(self):
        self.G = Graph()
        root = self.G.addNode('root')
        self.queue = [(BranchNode(TreeNode()), root)]

    def addNode(self, parent, child):
        child.cumW += parent.cumW
        child.cumV += parent.cumV
        child.flag += copy.deepcopy(parent.flag)
        child.label_set = child.label_set.union(parent.label_set)
        child.level = parent.level + 1
        return child
    
    def skipNode(self, parent):
        parent.level += 1
        return parent


def process():
    global arr
    global n
    arr = sorted(arr, reverse=True, key = lambda x: x.ratio)
    tree = BranchAndBound()
    bestV = 0
    bestNode = BranchNode(TreeNode())
    while len(tree.queue):
        u, parentNode = tree.queue.pop(0)
        if u.level == n - 1:
            continue
        v = tree.addNode(u, BranchNode(arr[u.level + 1]))
        u = tree.skipNode(u)
        
        if v.isValid() and v.bound() > bestV:
            vGraphNode = tree.G.addNode(
                f'value: {v.cumV}, weight:{v.cumW}',
                f'number of class = {len(v.label_set)}'
            )
            color = "white"
            description = ""
            if bestV < v.cumV:
                bestV = v.cumV
                bestNode = v
                color = "blue"
            tree.G.setNode(vGraphNode, color, description)
            tree.G.addEdge(parentNode, vGraphNode)
            tree.queue.append((v, vGraphNode))
        if u.bound() > bestNode.cumW:
            uGraphNode = tree.G.addNode(
                f'value: {u.cumV}, weight:{u.cumW}',
                f'number of class = {len(v.label_set)}'
            )
            tree.G.addEdge(parentNode, uGraphNode)
            tree.queue.append((u, uGraphNode))


    # Print Output
    with open(f"./output/2/Output_{testCaseNo}.txt", "w+") as f:
        f.write(str(bestNode.cumV) + '\n')
        output = []
        for index in range(0, n):
            output.append(str(int(index in bestNode.flag)))
        f.write(', '.join(output))




if __name__ == "__main__":
    input()
    start = time.time()
    process() 
    print("Execution time: ", time.time() - start)
