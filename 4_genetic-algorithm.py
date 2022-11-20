import random

M = 0
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
        self.presentation = random.randint(2, size = (n))

class Genetic:
    @staticmethod
    





if __name__ == "__main__":
    input()