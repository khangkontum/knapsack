import time
from tqdm import tqdm
import copy
import random
import graph

K = 100
epoch = 100
testCaseNo = 11

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
           
class State:
    def __init__(self, node):
        self.label_set = {node.label}
        self.flag_set = {node.index}
        self.weight = node.weight
        self.value = node.value
        self.ratio = node.ratio
    
    def addNode(self, node):
        tmp = copy.deepcopy(self)
        tmp.weight += node.weight
        tmp.value += node.value
        tmp.label_set.add(node.label)
        tmp.flag_set.add(node.index)
        return tmp

    def isValid(self):
        global W
        return self.weight < W

    def isAddable(self, node):
        tmp = copy.deepcopy(self)
        return (not node.index in tmp.flag_set) and tmp.addNode(node).isValid()
    
    def isFound(self, bestState):
        global m
        return len(self.label_set) == m and self.value > bestState.value
    
    def __str__(self):
        return "class<State> weight: " + str(self.weight) +\
           ", values: " + str(self.value,) +\
           ", labels: " + str(len(self.label_set))+\
            ", trace: " + str(self.flag_set)

           
def beam_search():
    global K
    global arr
    queue = []
    bestState = State(TreeNode())

    for j in tqdm(range(epoch)):
        G = graph.Graph()
        K_random_states = random.sample(range(1, n), K)
        for index in K_random_states:
            node = G.addNode(f"w: {arr[index].weight}, v: {arr[index].value}")
            queue.append((State(arr[index]), node))
            
        while(True and len(queue)):
            candidates = []
            while(len(queue)):
                state, parent = queue.pop(0)        
                for i in range(1, m + 1):
                    for candidateNode in bestOfLabel[i]:
                        if state.isAddable(candidateNode):
                            child = G.addNode(f"w: {candidateNode.weight}, v: {candidateNode.value}")
                            G.addEdge(parent, child)
                            candidates.append((state.addNode(candidateNode), child))

            is_ok = False
            for candidate, node  in candidates:
                if (len(candidate.label_set) >= 6):
                    print(candidateNode)
                if candidate.isFound(bestState):
                    is_ok = True
                    bestState = candidate
                    G.setNode(node, "red")
            if is_ok:
                break

            candidates = sorted(candidates, reverse=True, key=lambda x:x[0].ratio)
            queue = candidates[:min(len(candidates), K)]
            # print(bestState)


    print(bestState.value)
    print(*[int(x in bestState.flag_set) for x in range(0, n)])



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
        bestOfLabel = [[] for _ in range(m + 1)]
        for x in arr:
            bestOfLabel[x.label].append(x)
        for i in range(1, m + 1):
            bestOfLabel[i] = sorted(bestOfLabel[i], reverse = True, key=lambda x:x.ratio)

if __name__ == "__main__":
    input()
    start = time.time()
    beam_search()
    print("Execute Time: ", time.time() - start)

        


