#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

class TreeNode:
    def __init__(self, item = None, best_guess = 0): 
        self.value = item.value
        self.best_guess = best_guess
        self.left = None
        self.right = None
    
    @classmethod
    def ToString(self):
        return str(self.value)
    
#sort the list into a tree
def sort_node(root, item):
    
    if (root == None):
        root = TreeNode(item)
        return root
    
    if item.value < root.value:
        root.left = sort_node(root.left, item)
    elif item.value > root.value:
        root.right = sort_node(root.right, item)
        
    return root

def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    root = None
    
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    
    #determine if first loop
    i = 0
    # find the basket total if we removed weight constraint
    best_guess = sum(items[1]);
    
    #build binary tree
    for item in items:
        if i == 0:
            root = TreeNode(item, best_guess)
            i += 1
        sort_node(root, item)
    
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

