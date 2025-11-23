import re

s = open("/home/balerso/old study/PYege/24.txt").readline()
s = re.split(r'(.)\1', s)
print(max(len(p) for p in s) + 1)
