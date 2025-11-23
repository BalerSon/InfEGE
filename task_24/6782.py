string = open("/home/balerso/old study/PYege/24_txt/24-264.txt").readline()

cur_len = 1
max_len = 1

for i in range(len(string)):
    if (string[i].isalpha() and string[i - 1].isdigit()) or (string[i - 1].isalpha() and string[i].isdigit()):
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)
