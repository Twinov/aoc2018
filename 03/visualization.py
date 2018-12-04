from wand.image import Image
import sys

m = 1000
n = 1000
matrix = [[1] * n for i in range(m)]
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
                    if matrix[point2 + i][point1 + j] < 255:
                        matrix[point2 + i][point1 + j] += 40


with open('visualization.ppm', 'w') as vis:
    builder = 'P3\n' + str(m) + ' ' + str(n) + '\n255\n'
    for i in range(m):
        for j in range(n):
            if len(sys.argv) == 4:
                r = int(sys.argv[1]) * matrix[i][j]
                g = int(sys.argv[2]) * matrix[i][j]
                b = int(sys.argv[3]) * matrix[i][j]
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                builder += format(r, '03') + ' ' + format(g, '03') + ' ' + format(b, '03') + ' '
            else:
                builder += format(matrix[i][j], '03') + ' 000 000 '
        builder += '\n'
    vis.write(builder)

with Image(filename='visualization.ppm') as img:
    img.format ='png'
    img.save(filename='visualization.png')
