file_name = input()

morse_dict = {}

f_in = open(file_name, 'r')

for line in f_in:
    cleared_line = line.strip(' \n')
    value, key = cleared_line.split(' ')
    morse_dict[key] = value

f_in.close()

data = input()
morses = data.split('\n')
f_out = open('result.txt', 'w')

for morse in morses:
    res = ''
    codes = morse.split(' ')
    for code in codes:
        res += morse_dict[code]
    f_out.write(res)

f_out.close()
