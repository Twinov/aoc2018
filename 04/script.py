class Guard:
    def __init__(self, num):
        self.num = num
        self.total_awake = 0
        self.asleep_mins = [0] * 60
        self.most_asleep = -1

    def add_asleep(self, mins, awake_time):
        self.total_awake += mins
        for i in range(60):
            self.asleep_mins[i] += awake_time[i]
            if self.asleep_mins[i] > self.asleep_mins[self.most_asleep]:
                self.most_asleep = i

    def print_sched(self):
        builder = ''
        for i in range(60):
            if self.asleep_mins[i] < 10:
                builder += str(self.asleep_mins[i])
            else:
                builder += '>'
        return builder

guard_list = {}
with open('input') as file_input:
    string_list = []
    for line in file_input:
        if not len(line.strip()) == 0:
            string_list.append(line)
    string_list.sort()

    with open('sortedinput', 'w') as file:
        for s in string_list:
            file.write(s)

start_sleep = 0
current_id = 0
with open('sortedinput') as sorted_file:
    for line in sorted_file:
        if not len(line.strip()) == 0:
            if not line.find('#') == -1:
                current_id = int(line[line.find('#') + 1:line.find('b') - 1])
                if guard_list.get(current_id) == None:
                    guard_list[current_id] = Guard(current_id)
            elif not line.find('falls asleep') == -1:
                start_sleep = int(line[line.find(':') + 1:line.find(']')])
            else:
                end_sleep = int(line[line.find(':') + 1:line.find(']')])
                temp_list = [0] * 60
                for i in range(60):
                    if i >= start_sleep and i < end_sleep:
                        temp_list[i] += 1
                guard_list[current_id].add_asleep(end_sleep - start_sleep, temp_list)

print('      Hour: 000000000011111111112222222222333333333344444444445555555555')
print('  ID   Min: 012345678901234567890123456789012345678901234567890123456789')
for key, guard in guard_list.iteritems():
    print('{:04} Awake: {}'.format(key, guard.print_sched()))

guard_hash = 0
guard_most_asleep = 0
guard_most_asleep_mins = 0
part2hash = 0
min_most_freq_asleep = -1
min_most_freq_asleep_tot = -1
guard_at_min = 0
for key, guard in guard_list.iteritems():
    if guard.total_awake > guard_most_asleep_mins:
        guard_most_asleep_mins = guard.total_awake
        guard_most_asleep = key
    if guard.asleep_mins[guard.most_asleep] > min_most_freq_asleep_tot:
        min_most_freq_asleep_tot = guard.asleep_mins[guard.most_asleep]
        guard_at_min = key
        min_most_freq_asleep = guard.most_asleep
guard_hash = guard_most_asleep * guard_list[guard_most_asleep].most_asleep
part2hash = guard_at_min * min_most_freq_asleep
print('Part 1 hash: {} \nPart 2 hash: {}'.format(guard_hash, part2hash))


