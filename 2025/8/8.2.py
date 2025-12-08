import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

vectors = []
for line in lines:
    vectors.append(line.strip())

# get all groups of 2 vectors
from itertools import combinations

groups = combinations(vectors, 2)
print(f"Total groups: {len(list(combinations(vectors, 2)))}")

groups_with_distances = []
for v1, v2 in groups:
    v1_arr = np.array([int(c) for c in v1.strip().split(",")])
    v2_arr = np.array([int(c) for c in v2.strip().split(",")])
    euclid_dist = float(np.linalg.norm(v1_arr - v2_arr))
    groups_with_distances.append((v1, v2, euclid_dist))

# Sort by distance
groups_with_distances.sort(key=lambda x: x[2])

# make circuits
circuits = []

latest_connection = None
first_one = False
for v1, v2, dist in groups_with_distances:
    if len(circuits) == 0:
        circuits.append([v1, v2])
        first_one = True
        continue


    not_added = True
    for c in circuits:
        if v1 in c and v2 in c:
            # both already in circuit
            not_added = False
            break
        elif v1 in c:
            if v2 not in c:
                # check if v2 is in any other circuit
                merged = False
                for other_c in circuits:
                    if other_c != c and v2 in other_c:
                        # merge circuits
                        c.extend(other_c)
                        circuits.remove(other_c)
                        merged = True
                        latest_connection = (v1, v2)
                        break
                if not merged:
                    latest_connection = (v1, v2)
                    c.append(v2)
                not_added = False
                break
        elif v2 in c:
            if v1 not in c:
                # check if v1 is in any other circuit
                merged = False
                for other_c in circuits:
                    if other_c != c and v1 in other_c:
                        # merge circuits
                        c.extend(other_c)
                        circuits.remove(other_c)
                        merged = True
                        latest_connection = (v1, v2)
                        break
                if not merged:
                    latest_connection = (v1, v2)
                    c.append(v1)
                not_added = False
                break
    if not_added:
        # neither in circuit
        # create a new circuit
        circuits.append([v1, v2])

print(f"Total circuits: {len(circuits)}")
# print(circuits)

print(f"{latest_connection=}")

a = int(latest_connection[0].split(",")[0])
b = int(latest_connection[1].split(",")[0])
print(a*b)

