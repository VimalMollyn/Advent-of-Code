import numpy as  np 

file_name = "input.txt"

# read the sample input
with open(file_name) as f:
    data = f.readlines()

# convert the data into a numpy array
smoke_flows = []
for line in data:
    line_data = [int(x) for x in line.strip()]
    smoke_flows.append(line_data)

smoke_flows = np.array(smoke_flows).astype(np.float64)
shape = smoke_flows.shape

# pad the edge value
smoke_flows = np.pad(
        smoke_flows,
        ((1,1), (1,1)),
        'constant', constant_values=(np.inf,np.inf))

print(smoke_flows)
# find the low points
low_points = []
equal_points = []

for i in range(1, shape[0]+1):
    for j in range(1, shape[1]+1):
        # get all the numbers around this index
        sub_arr = smoke_flows[i-1:i+2, j-1:j+2].copy()
        sub_arr[1, 1] = np.inf

        # get the min of the sub array
        min_sub_array = sub_arr.flatten().min()

        # check if the min is smaller than the value
        if smoke_flows[i, j] < min_sub_array:
            low_points.append(smoke_flows[i, j])
        elif smoke_flows[i, j] == min_sub_array:
            equal_points.append(smoke_flows[i, j])
        
print(int(np.sum(np.array(low_points) + 1)))
print(int(np.sum(np.array(equal_points) + 1)))




