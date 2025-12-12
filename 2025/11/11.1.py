import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

class Node:
    def __init__(self, value):
        self.inputs = []
        self.outputs = []
        self.value = value

    def add_input(self, _input):
        self.inputs.append(_input)

    def add_ouput(self, _output):
        self.outputs.append(_output)

nodes = {}
for line in lines:
    print(line.strip())
    parent, children = line.strip().split(": ")
    children_list = children.split(" ")
    print(parent, children_list)
    print()

    if parent not in nodes.keys():
        parent_node = Node(parent)
    else:
        parent_node = nodes[parent]

    for child in children_list:
        if child not in nodes.keys():
            child_node = Node(child)
        else:
            child_node = nodes[child]

        parent_node.add_ouput(child_node)
        child_node.add_input(parent_node)
        nodes[child] = child_node

    nodes[parent] = parent_node

# get number of paths from "you" to "out". start from "out" and go backwards to "you"

# TOO SLOW

# nodes_left = [nodes["out"]]

# count = 0
# while len(nodes_left) > 0:
#     current_node = nodes_left.pop(0)
#     print("Current node:", current_node.value, f"{len(nodes_left)=}")
#
#     if current_node.value == "you":
#         print("Found path to 'you'")
#         count += 1
#     elif len(current_node.inputs) == 0:
#         print("No more inputs to explore from", current_node.value)
#         continue
#
#     for input_node in current_node.inputs:
#         nodes_left.append(input_node)
# print(count)

for node in nodes.values():
    print(f"{node.value=}")

    print("  inputs:", [input_node.value for input_node in node.inputs])
    print("  outputs:", [output_node.value for output_node in node.outputs])

num_paths = {"out": 1}
def num_paths_from_X_to_out(X):
    print(f"num_paths_from_X_to_out({X}) called")
    for output in nodes[X].outputs:
        print(f"  output: {output.value}")
    if X in num_paths:
        print(f"  found cached value for {X}: {num_paths[X]}")
        return num_paths[X]
    
    return sum(num_paths_from_X_to_out(node.value) for node in nodes[X].outputs)

print(num_paths_from_X_to_out("you"))
