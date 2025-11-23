import re

s = "AKJBWOINOIWECFFIOFFNLLDNNERQOWPETRUONQCNERIOSNNLF"

result = re.sub('[ABCD]', ' ', s).split()

print(max(len(res) for res in result))
