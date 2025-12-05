import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

# ranges = []

class Set:
    def __init__(self, start, end):
        # both are inclusive
        self.start = start
        self.end = end

    def union(self, other_set):
        # check if overlapping
        if self.end < other_set.start - 1 or other_set.end < self.start - 1:
            # not overlapping
            return [self, other_set]
        elif self.start <= other_set.start and self.end >= other_set.end:
            # self contains other_set
            return [self]
        elif other_set.start <= self.start and other_set.end >= self.end:
            # other_set contains self
            return [other_set]
        elif self.start <= other_set.start and self.end<= other_set.end:
            # overlapping, self starts first
            return [Set(self.start, other_set.end)]
        elif other_set.start <= self.start and other_set.end <= self.end:
            # overlapping, other_set starts first
            return [Set(other_set.start, self.end)]
    def length(self):
        return self.end - self.start + 1
    
    def __repr__(self):
        return f"[{self.start}, {self.end}]"


all_sets = []
for line in lines:
    line = line.strip()
    if line == "":
        # ranges_done = True
        break
    start, end = line.split("-")
    start = int(start)
    end = int(end)
    # ranges.append(set(range(start, end+1)))
    new_set = Set(start, end)
    all_sets.append(new_set)

# sort all sets based on the start
print(f"unsorted {all_sets}")
all_sets.sort(key=lambda x: x.start)
print(f"sorted {all_sets}")

length_before = len(all_sets)
while True:
    for i in range(length_before):
        # reduce sets in pairs
        a_set = all_sets.pop(0)
        b_set = all_sets.pop(0)

        union_sets = a_set.union(b_set)
        all_sets.extend(union_sets)
         
    # sort again
    all_sets.sort(key=lambda x: x.start)
    new_length = len(all_sets)
    if new_length == length_before:
        # no more reductions possible
        break
    else:
        length_before = new_length
        print("Reduced to", new_length, "sets")

print(all_sets)
print(sum([x.length() for x in all_sets]))

