import re

s = open("/home/balerso/old study/PYege/24_txt/24-360.txt").readline()

pattern = r'[02468]([A-Z])\1*[02468]'
res = re.finditer(pattern, s)

a = []
for i in res:
    string = i.group()
    a.append(string)
print(max(len(i) for i in a))
