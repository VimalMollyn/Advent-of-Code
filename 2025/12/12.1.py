import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

# get present ids
i = 0
shapes = {}
shape_areas = {}
print(len(lines))
total = 0
while i < len(lines):
    line = lines[i]
    if len(line.strip()) == 2:
        # this is a shaped id line
        shape_id = line.split(":")[0].strip()

        # read the next 3 lines
        shape_lines = [x.strip() for x in lines[i+1:i+4]]
        shape_lines = np.array([list(x) for x in shape_lines])
        shapes[shape_id] = shape_lines

        shape_area = np.sum(shape_lines == "#")
        shape_areas[shape_id] = shape_area


        i += 4
        continue
    elif line.strip() == "":
        # print("Skipping blank line")
        i += 1
    else:
        # print("Processing arrangement line:", line)
        # now we're reading arrangements
        total_area, shapes_str = line.strip().split(": ")

        w, h = (int(x) for x in total_area.split("x"))
        total_area = w * h
        # print("Total area:", total_area)

        shape_id_counts = [int(s.strip()) for s in shapes_str.split(" ")]

        # calculate total area of shapes
        total_shapes_area = 0
        for j, count in enumerate(shape_id_counts):
            shape_id = str(j)
            shape_area = shape_areas[shape_id]
            total_shapes_area += shape_area * count

        if total_shapes_area <= total_area:
            total += 1
            # print("YES", line, total_shapes_area, total_area)

        i+=1

print("Total valid arrangements:", total)
