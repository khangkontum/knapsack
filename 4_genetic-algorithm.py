import math
import numpy as np
from tqdm import tqdm

K = 1000
testCaseNo = 11
epoch = 10000

W = 0
m = 0
n = 0
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
        
class Individual:
    def __init__(self):
        global n
        self.presentation = np.random.randint(2, size = (n))
    
    def __str__(self) -> str:
        return "".join([str(x) for x in self.presentation])
    
    def fitness(self) ->float:
        global W
        global m
        fit = 0
        weight = 0
        label_set = set()
        for index, bit in enumerate(self.presentation):
            fit += arr[index].value * bit 
            label_set.add(arr[index].label)
            weight += arr[index].weight * bit
        return fit * float(weight < W and len(label_set) == m)

    staticmethod
    def join(A, B, offset):
        tmp = Individual()
        tmp.presentation = np.concatenate((A.presentation[:offset], B.presentation[offset:]))
        return tmp


class Genetic:
    def __init__(self, population = 10):
        self.active_individuals = [Individual() for _ in range(population)]
    
    def cal_probs(self):
        self.probs = [x.fitness() for x in self.active_individuals]
        if sum(self.probs) == 0:
            self.probs = []
            return
        self.probs = self.probs / sum(self.probs)

    def selection(self):
        global n
        return tuple(np.random.choice(self.active_individuals, p = self.probs, size = 2))
    
    def cross_over(self, A, B):
        global n
        offset = np.random.randint(0, n)
        childA = Individual.join(A, B, offset)
        childB = Individual.join(B, A, offset)
        return (childA, childB)

    def mutation(self):
        global n
        for index in range(len(self.active_individuals)):
            rand_offset = np.random.randint(0, n)
            self.active_individuals[index].presentation[rand_offset] = float(not self.active_individuals[index].presentation[rand_offset])

        

def input():
    global W, m
    global n
    global arr, bestOfLabel
    with open(f'./input/Input_{testCaseNo}.txt', 'r') as f:
        W = float(f.readline())
        m = float(f.readline())
        weights = f.readline().split(', ')
        values = f.readline().split(', ')
        labels = f.readline().split(', ')
        n = len(labels)
        i = 0
        for w, v, c in zip(weights, values, labels):
            arr.append(TreeNode(float(w), float(v), float(i), float(c)))
            i += 1

def process():
    global K
    global epoch
    genetic = Genetic(K)
    bestIndivudual = Individual()
    for _ in tqdm(range(epoch)):
        for individual in genetic.active_individuals:
            if individual.fitness() > bestIndivudual.fitness():
                bestIndivudual = individual
        genetic.cal_probs()
        # Population have no good state
        if (len(genetic.probs) == 0):
            genetic = Genetic()
            continue
        tmp = []
        for _ in range(0, K, 2):
            a, b = genetic.selection()
            a, b = genetic.cross_over(a, b)
            tmp.append(a)
            tmp.append(b)

        if K % 2 == 1:
            a, _ = genetic.selection()
            tmp.append(a)
        genetic.active_individuals = tmp
        genetic.mutation()

    if bestIndivudual.fitness() != 0:
        print(bestIndivudual.fitness())
        print(bestIndivudual.presentation)
    else:
        print("not found")



if __name__ == "__main__":
    input()
    process()