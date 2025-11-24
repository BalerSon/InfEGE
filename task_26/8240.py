file = open("/home/balerso/infEGE/infEGE/task_26/26-174.txt")
n = file.readline()

points = {}

for line in file:
    a, b = map(int, line.split())
    if b not in points:
        points[b] = set()
    points[b].add(a)
    
print(points)
    
def find_max_subseq_len(sequence):
    k = 1
    cur_k = 1
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] == 1:
            cur_k += 1
            k = max(k, cur_k)
        else:
            cur_k = 1
    return k
    
m = 0
    
for i in points:
    points[i] = sorted(points[i])
    max_len_subseq = find_max_subseq_len(points[i])
    if max_len_subseq > m:
        index = i
        m = max_len_subseq
    elif max_len_subseq == m and max_len_subseq > 0:
        index = min(index, i)

print(m, index)