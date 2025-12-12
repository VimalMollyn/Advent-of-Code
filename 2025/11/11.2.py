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

# TOO SLOW again
# sort topo
indegrees = {}
for node in nodes.values():
    indegrees[node.value] = len(node.inputs)

queue = [u for u in indegrees.keys() if indegrees[u] == 0]

topo_sorted = []
while len(queue) > 0:
    current_value = queue.pop(0)
    topo_sorted.append(current_value)

    current_node = nodes[current_value]
    for output_node in current_node.outputs:
        indegrees[output_node.value] -= 1
        if indegrees[output_node.value] == 0:
            queue.append(output_node.value)

print("Topologically sorted nodes:", topo_sorted)
topo_sorted.reverse()

def num_paths_from_A_to_B(A, B):
    ways = {node: 0 for node in nodes.keys()}
    ways[B] = 1

    for node in topo_sorted:
        current_node = nodes[node]
        for input_node in current_node.inputs:
            ways[input_node.value] += ways[current_node.value]
    return ways[A]

# print(num_paths_from_A_to_B("you", "out"))
svr_dac = num_paths_from_A_to_B("svr", "dac")
dac_fft = num_paths_from_A_to_B("dac", "fft")
fft_out = num_paths_from_A_to_B("fft", "out")

svr_fft = num_paths_from_A_to_B("svr", "fft")
fft_dac = num_paths_from_A_to_B("fft", "dac")
dac_out = num_paths_from_A_to_B("dac", "out")

print(svr_dac * dac_fft * fft_out + svr_fft * fft_dac * dac_out)

