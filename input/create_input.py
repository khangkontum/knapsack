import sys
import os
import random

if os.path.dirname(os.path.abspath(__file__)) in sys.path:
    sys.path.remove(os.path.dirname(os.path.abspath(__file__)))

def main(num_small, num_large):
    for i in range(num_small):
        capacity_w = random.randrange(100, 1000, 17)
        num_classes_m = random.randint(1,6)
        n = random.randint(10,40)
        weights = [None] * n
        values = [None] * n
        classes = [None] * n
        for j in range(n):
            weights[j] = random.randrange(1, capacity_w - 15, 3)
            values[j] =  random.randrange(1, capacity_w - 15, 3)
            if num_classes_m == 1:
                classes[j] = 1
            else:
                classes[j] = random.randint(1, num_classes_m)
        fileName = "INPUT_" + str(i+1) + ".txt"
        f =  open(fileName, 'w')
        f.write(str(capacity_w) + '\n')
        f.write(str(num_classes_m) + '\n')
        f.write(str(weights).replace('[','').replace(']','') + '\n')
        f.write(str(values).replace('[','').replace(']','') + '\n')
        f.write(str(classes).replace('[','').replace(']','') + '\n')
    
    for i in range(num_large):
        capacity_w = random.randrange(1000, 10000, 29)
        num_classes_m = random.randint(5, 10)
        n = random.randint(50, 1000)
        weights = [None] * n
        values = [None] * n
        classes = [None] * n
        for j in range(n):
            weights[j] = random.randrange(10, capacity_w - 53, 23)
            values[j] =  random.randrange(10, capacity_w - 53, 23)
            if num_classes_m == 1:
                classes[j] = 1
            else:
                classes[j] = random.randint(1, num_classes_m)
        fileName = "INPUT_" + str(num_small + i + 1) + ".txt"
        f =  open(fileName, 'w')
        f.write(str(capacity_w) + '\n')
        f.write(str(num_classes_m) + '\n')
        f.write(str(weights).replace('[','').replace(']','') + '\n')
        f.write(str(values).replace('[','').replace(']','') + '\n')
        f.write(str(classes).replace('[','').replace(']','') + '\n')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: create_input.py <num_small_dataset> <num_large_dataset>")
        sys.exit(0)
    main(max(5,int(sys.argv[1])), max(5,int(sys.argv[2])))