import string
def bad_func(s):
    not_finished = True
    while not_finished:
        iteration = 0
        for i in range(26):
            pair_chars = string.ascii_uppercase[i] + string.ascii_lowercase[i]
            s = s.replace(pair_chars, '')
        for i in range(26):
            pair_chars = string.ascii_lowercase[i] + string.ascii_uppercase[i]
            s = s.replace(pair_chars, '')
        not_finished = False
        for c in s:
            if not iteration == 0:
                if abs(ord(c) - ord(s[iteration - 1])) == 32:
                    not_finished = True
            iteration += 1
    return s


answer_string = ''
lowest_length = 50000
with open('input') as file_input:
    answer_string = bad_func(file_input.read().strip())
    print('Part 1 polymer length: {}'.format(len(answer_string)))
    for i in range(26):
        temp_string = answer_string
        temp_string = temp_string.replace(string.ascii_uppercase[i], '')
        temp_string = temp_string.replace(string.ascii_lowercase[i], '')
        length = len(bad_func(temp_string))
        if length < lowest_length:
            lowest_length = length
    print('Part 2 lowest length: {}'.format(lowest_length))


