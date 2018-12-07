def manahatten_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

num_coords = 0
map_size_x = 0
map_size_y = 0
inputfile = 'input1'
with open(inputfile) as file:
    index1 = 0
    for line in file:
        if not len(line.strip()) == 0:
            if int(line[:line.find(',')]) > map_size_x:
                map_size_x = int(line[:line.find(',')])
            if int(line[line.find(',') + 2:]) > map_size_y:
                map_size_y = int(line[line.find(',') + 2:])
            num_coords = index1 + 1
        index1 += 1

map_size_y = 10
map_size_x = 9
coords = [[0 for x in range(2)] for y in range(num_coords)]
big_map = [[0 for x in range(map_size_x)] for y in range(map_size_y)]
coords_area = [0] * num_coords
nums_on_edge = [0] * num_coords
with open(inputfile) as file_input:
    index = 0
    for line in file_input:
        if not len(line.strip()) == 0:
            coords[index][0] = int(line[:line.find(',')])
            coords[index][1] = int(line[line.find(',') + 2:])
        index += 1
print(coords)

for i in range(map_size_y):
    for j in range(map_size_x):
        for k in range(len(coords)):
            if coords[k][0] == j and coords[k][1] == i:
                print(coords[k])
                big_map[j-1][i-1] = k
    print(i)

print_builder = ''
for i in range(map_size_y):
    for j in range(map_size_x):
        print_builder += str(big_map[j-1][i-1]).zfill(2) + ' '
    print_builder += '\n'
print(print_builder)


for i in range(map_size_y-1):
    for j in range(map_size_x -1):
        shortest = 0
        shortest_dist = 500
        equal = False
        for index in range(len(coords)):
            dist = manahatten_distance([j, i], coords[index])
            if dist < shortest_dist:
                shortest = index + 1
                shortest_dist = dist
                equal = False
            elif dist == shortest_dist:
                equal = True
        big_map[j][i] = shortest
        if not equal:
            coords_area[shortest - 1] += 1
        if equal:
            big_map[j][i] = 0
        if i == 0 or j == 0 or j == map_size_x - 1 or i == map_size_y - 1:
            nums_on_edge[shortest - 1] = 1
#            print('eliminated {}'.format(shortest -1))


print_builder = ''
for i in range(map_size_y-1):
    for j in range(map_size_x-1):
        print_builder += str(big_map[j][i]).zfill(2) + ' '
    print_builder += '\n'
print(print_builder)

coords_area.append(0)
max_area = len(coords_area) - 1
for i in range(len(coords)):
    if coords_area[i] > coords_area[max_area]:
        if not nums_on_edge[i] == 1:
            max_area = i
print(coords_area)
print('Max area: {} with coord #: {}'.format(coords_area[max_area + 1], max_area + 1))
