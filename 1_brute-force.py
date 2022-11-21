import itertools
import numpy as np

K = 10
epoch = 100
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

    lst = map(list, itertools.product([0,1], repeat = n))
    for i in lst:
        bitset = np.asarray(i)
        curW, curV = 0, 0
        for index, bit in enumerate(bitset):
            curW += bit * arr[index].weight
            curV += bit * arr[index].value
        if curW <= W and curV > bestV:
            bestV = curV
            bestSol = bitset

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



if __name__ == "__main__":
    input()
    brute()
    print(bestV)
    print(bestSol)

