total = 0
prev_totals = []
keep_read = True
iteration = 0
while keep_read:
    print(iteration)
    with open('input') as inputfile:
        for line in inputfile:
            if not len(line.strip()) == 0:
                if keep_read:
                    total += int(line)
                    if not total in prev_totals:
                        prev_totals.append(total)
                    else:
                        keep_read = False
    iteration += 1
for num in prevTotals: #print totals
    print('{} freq {}'.format(num, prevTotals.count(num)))
print(total)

