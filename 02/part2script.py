box_list = []
correct_boxes = []
with open('input') as inputfile:
    for line in inputfile:
        box_list.append(line)
        if not len(line.strip()) == 0:
            for box in box_list:
                num_not_match = 0
                for i in range(len(line)):
                    if box[i] != line[i]:
                        num_not_match += 1
                if num_not_match == 1:
                    correct_boxes.append(line)
                    correct_boxes.append(box)
#        box_list.append(line)
for box in correct_boxes:
    print(box)
