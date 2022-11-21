import itertools
import time
import numpy as np

testCaseNo = 0

W = 0
N = 10005
m = 0 
n = 0
bestOfLabel = []
bestV = 0
bestSol = []
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


def brute():
    global n
    global arr
    global W
    global bestV
    global bestSol
    global m

    lst = map(list, itertools.product([0,1], repeat = n))
    for i in lst:
        bitset = np.asarray(i)
        curW, curV = 0, 0
        label_set = set()
        for index, bit in enumerate(bitset):
            curW += bit * arr[index].weight
            curV += bit * arr[index].value
            if bit == 1:
                label_set.add(arr[index].label)
        if curW <= W and curV > bestV and len(label_set) == m:
            bestV = curV
            bestSol = bitset
        

def input():
    global W, m
    global n
    global arr, bestOfLabel

    with open(f'./input/Input_{testCaseNo}.txt', 'r') as f:
    # with open(f'./inputTree/Input_Tree_0.txt', 'r') as f:
        W = int(f.readline())
        m = int(f.readline())
        weights = f.readline().split(', ')
        values = f.readline().split(', ')
        labels = f.readline().split(', ')
        n = len(labels)
        print("n = ", n)
        i = 0
        for w, v, c in zip(weights, values, labels):
            arr.append(TreeNode(int(w), int(v), int(i), int(c)))
            i += 1



if __name__ == "__main__":
    input()
    start = time.time()
    brute()
    with open(f"./output/1/Output_{testCaseNo}.txt", "w+") as f:
        f.write(str(bestV) + '\n')
        f.write(', '.join([str(x) for x in bestSol]))
    print("Execution time", time.time() - start)

