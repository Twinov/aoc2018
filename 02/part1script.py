import collections

num_dubs = 0
num_trips = 0
ya_dub = False
ya_trip = False
with open('input') as inputfile:
    for line in inputfile:
        print(line)
        for freq in collections.Counter(line):
            if collections.Counter(line)[freq] == 2 and not ya_dub:
                num_dubs += 1
                print('dub')
                ya_dub = True
            elif collections.Counter(line)[freq] == 3 and not ya_trip:
                num_trips += 1
                print('trip')
                ya_trip = True
        ya_dub = False
        ya_trip = False

print(num_dubs * num_trips)
