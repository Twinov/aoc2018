import sys
import string

sys.setrecursionlimit(20000)

def remove_upper_lower(s):
    chars_removed = 0
    complete = True
    iteration = 0
    done_once = False
    for c in s:
        if not iteration == 0 and not done_once:
            if abs(ord(c) - ord(s[iteration - 1])) == 32:
                complete = False
                done_once = True
                s = s[:iteration - 1] + s[iteration + 1:]
        iteration += 1

    if complete == True:
        return s
    else:
        return remove_upper_lower(s)

answer_string = ''
lowest_length = 50000
with open('input') as file_input:
    answer_string = remove_upper_lower(file_input.read().strip())
    print(answer_string)
    print(len(answer_string))
    for i in range(26):
        temp_string = answer_string
        temp_string = temp_string.replace(string.ascii_uppercase[i], '')
        temp_string = temp_string.replace(string.ascii_lowercase[i], '')
        length = len(remove_upper_lower(temp_string))
        if length < lowest_length:
            lowest_length = length
    print('Lowest polymer length is: {}'.format(lowest_length))
    iteration = 0
    for c in answer_string:
        if not iteration == 0:
            if abs(ord(c) - ord(s[iteration - 1])) == 32:
                print('failed')
