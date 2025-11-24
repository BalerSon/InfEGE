file = open("/home/balerso/infEGE/infEGE/task_26/26-8239.txt")
windows = int(file.readline())
citizens = int(file.readline())

k = 0
freq = {i: [] for i  in range(1, windows + 1)}

"""a - время начала приема, b - время окончания приема"""
for line in file:
    a, b = map(int, line.split())
    cur_count = 0
    for i in range(len(freq)):
        