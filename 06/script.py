num_coords = 6
coords = [[0 for x in range(2)] for y in range(num_coords)]
inputfile = 'input1'
map_size_x = 0
map_size_y = 0
with open(inputfile) as file_input:
        index = 0
        for line in file_input:
            if not len(line.strip()) == 0:
                if int(line[:line.find(',')]) > map_size_x:
                    map_size_x = int(line[:line.find(',')])
                if int(line[line.find(',') + 2:]) > map_size_y:
                    map_size_y = int(line[line.find(',') + 2:])
#map_size_x = 9 
#map_size_y = 10
map_size_x += 1
map_size_y += 1
print(map_size_x)
print(map_size_y)
with open(inputfile) as file_input:
    index = 0
    for line in file_input:
        if not len(line.strip()) == 0:
            coords[index][0] = int(line[:line.find(',')])
            coords[index][1] = int(line[line.find(',') + 2:])
        index += 1
print(coords)

big_map = [0] * map_size_x * map_size_y
print(len(big_map))
xc = -1
yc = -1
coords_area = [0] * num_coords
nums_on_edge = [0] * num_coords
for i in range(len(big_map)):
    if xc == -1:
        xc = 0
        yc = 0
    elif xc == map_size_x:
        yc += 1
        xc = 0
    else:
        xc += 1

 #   print('[{}, {}]'.format(xc, yc))
    shortest = 0
    shortest_dist = 500
    equal = False
    for index in range(len(coords)):
        dist = abs(xc - coords[index][0]) + abs(yc - coords[index][1]) 
        if dist < shortest_dist:
            shortest = index + 1
            shortest_dist = dist
            equal = False
        elif dist == shortest_dist:
            equal = True
    big_map[i] =  shortest
    if not equal:
        coords_area[shortest - 1] += 1
    if equal:
        big_map[i] = 0
    if xc == 0 or yc == 0 or xc == map_size_x or yc == map_size_y:
        nums_on_edge[shortest - 1] = 1
        print(shortest-1)
xc = -1
yc = -1
print_builder = ''
for i in range(len(big_map)):
    if xc == -1:
        xc = 0
        yc = 0
    elif xc == map_size_x:
        print_builder += '\n'
        yc += 1
        xc = 0
    else:
        xc += 1
    print_builder += str(big_map[i]).zfill(2) + ' '

print(print_builder)

coords_area.append(0)
max_area = len(coords_area) - 1
for i in range(len(coords)):
    if coords_area[i] > coords_area[max_area]:
        if not nums_on_edge[i] == 1:
            max_area = i
print(coords_area)
print('Max area: {} with coord #: {}'.format(coords_area[max_area + 1], max_area + 1))