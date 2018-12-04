import numpy

m = 1000
n = 1000
matrix = [[0] * n for i in range(m)]
overlaps = 0
correct_num = 0
with open('input') as file_input:
    for line in file_input:
        if not len(line.strip()) == 0:
            point1 = int(line[line.find('@') + 2:line.find(',')])
            point2 = int(line[line.find(',') + 1:line.find(':')])

            hor = int(line[line.find(':') + 2:line.find('x')])
            vert = int(line.strip()[line.find('x') + 1::])

            num = int(line[line.find('#') + 1:line.find('@') - 1])

            for i in range(vert):
                for j in range(hor):
                    if matrix[point2 + i][point1 + j] == 0:
                        matrix[point2 + i][point1 + j] = num
                    elif not matrix[point2 + i][point1 + j] == 'X':
                        matrix[point2 + i][point1 + j] = 'X'
                        overlaps += 1
#print the array
#for i in range(m):
#    line = ''
#    for j in range(n):
#        line += str(matrix[i][j])
#    print(line)

with open('input') as file_input:
    for line in file_input:
        if not len(line.strip()) == 0:
            point1 = int(line[line.find('@') + 2:line.find(',')])
            point2 = int(line[line.find(',') + 1:line.find(':')])

            hor = int(line[line.find(':') + 2:line.find('x')])
            vert = int(line.strip()[line.find('x') + 1::])

            num = int(line[line.find('#') + 1:line.find('@') - 1])

            wrong_num = False
            for i in range(vert):
                for j in range(hor):
                    if matrix[point2 + i][point1 + j] == 'X':
                        wrong_num = True
            if not wrong_num:
                correct_num = num

print(overlaps)
print(correct_num)
